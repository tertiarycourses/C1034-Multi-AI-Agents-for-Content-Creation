"""Transparent retrieval helpers used by the RAG labs.

The teaching index is intentionally lexical so learners can inspect every
token, score and source identifier. The Learner Guide then maps the same
retrieval contract to vector memory implementations.
"""

from __future__ import annotations

import json
import math
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


TOKEN_RE = re.compile(r"[a-z0-9]+")
SECTION_RE = re.compile(r"^## \[([^]]+)]\s+(.+)$", re.MULTILINE)
STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "do", "does",
    "for", "from", "how", "in", "is", "it", "of", "on", "or", "should",
    "the", "to", "what", "when", "where", "which", "with",
}
NORMAL_FORMS = {
    "approvals": "approval",
    "required": "require",
    "requires": "require",
    "requirements": "require",
}


@dataclass(frozen=True)
class Chunk:
    source_id: str
    title: str
    text: str
    tokens: tuple[str, ...]


def tokenize(text: str) -> tuple[str, ...]:
    tokens: list[str] = []
    for raw in TOKEN_RE.findall(text.lower()):
        if raw in STOP_WORDS:
            continue
        token = NORMAL_FORMS.get(raw, raw)
        if token.endswith("ies") and len(token) > 4:
            token = token[:-3] + "y"
        elif token.endswith("s") and len(token) > 4 and not token.endswith("ss"):
            token = token[:-1]
        tokens.append(token)
    return tuple(tokens)


def parse_handbook(path: Path) -> list[Chunk]:
    text = path.read_text(encoding="utf-8")
    matches = list(SECTION_RE.finditer(text))
    chunks: list[Chunk] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[match.end():end].strip()
        chunks.append(
            Chunk(
                source_id=match.group(1),
                title=match.group(2).strip(),
                text=body,
                tokens=tokenize(f"{match.group(2)} {body}"),
            )
        )
    if not chunks:
        raise ValueError(f"No '[SOURCE-ID]' sections found in {path}")
    return chunks


def save_index(chunks: Iterable[Chunk], path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = [asdict(chunk) for chunk in chunks]
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def load_index(path: Path) -> list[Chunk]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return [Chunk(tokens=tuple(item["tokens"]), source_id=item["source_id"], title=item["title"], text=item["text"]) for item in payload]


def _idf(chunks: list[Chunk], token: str) -> float:
    documents_with_token = sum(token in set(chunk.tokens) for chunk in chunks)
    return math.log((1 + len(chunks)) / (1 + documents_with_token)) + 1.0


def search(chunks: list[Chunk], query: str, top_k: int = 3) -> list[dict[str, object]]:
    query_tokens = set(tokenize(query))
    if not query_tokens:
        return []
    query_weight = sum(_idf(chunks, token) for token in query_tokens)
    ranked: list[dict[str, object]] = []
    for chunk in chunks:
        chunk_tokens = set(chunk.tokens)
        matched = query_tokens & chunk_tokens
        weighted_overlap = sum(_idf(chunks, token) for token in matched)
        # Rank by weighted query coverage. This prevents long source sections
        # from being penalised and stops generic document length from
        # outweighing a distinctive term such as "vpn".
        score = weighted_overlap / max(query_weight, 1.0)
        ranked.append(
            {
                "source_id": chunk.source_id,
                "title": chunk.title,
                "score": round(score, 4),
                "matched_terms": sorted(matched),
                "text": chunk.text,
            }
        )
    ranked.sort(key=lambda item: (-float(item["score"]), str(item["source_id"])))
    return [item for item in ranked[:top_k] if float(item["score"]) > 0]


def grounded_answer(query: str, results: list[dict[str, object]], minimum_score: float = 0.08) -> dict[str, object]:
    usable = [result for result in results if float(result["score"]) >= minimum_score]
    if not usable:
        return {
            "status": "insufficient_evidence",
            "query": query,
            "answer": "I do not have enough handbook evidence to answer this request.",
            "sources": [],
        }
    best = usable[0]
    return {
        "status": "grounded",
        "query": query,
        "answer": f"{best['text']} [{best['source_id']}]",
        "sources": [item["source_id"] for item in usable],
    }
