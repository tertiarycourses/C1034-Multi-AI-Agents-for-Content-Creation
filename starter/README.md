# OpsDesk lab kit

This package is the executable companion to the eight C1034 labs. Run commands from the repository root after `python -m pip install -e starter`; every lab path and checkpoint assumes that working directory.

The default `--offline` route still uses AutoGen AgentChat. It substitutes `ReplayChatCompletionClient` for a paid model so the message, tool and team behaviours are reproducible. Optional live calls require `OPENAI_API_KEY` in the environment and are deliberately separate from the offline evidence.

Generated lab evidence is written to the repository-level `.course_state/` directory, which is ignored by Git.

Lab 6 generates and validates a team contract. Lab 8 generates an operations record that must name owners, signals, pause triggers, recovery and an explicit decision. The final release check reports technical readiness separately and cannot emit `READY FOR GUIDED DEMO` until that record is complete and valid.
