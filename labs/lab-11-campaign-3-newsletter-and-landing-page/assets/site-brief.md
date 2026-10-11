# Website brief — Horizon Wealth Planning (the reference for every Horizon page)

One self-contained page, web/site/index.html, published as a Claude artifact
(Lab 1). The artifact viewer runs it in a sandboxed frame with its own
security policy, so: no frame-busting script, no Content-Security-Policy
meta tag, fonts only from Google Fonts, every image as inline SVG, no
external scripts, no backend. Sections in order:

1. **Header** — Sunny logo + "Horizon Wealth", links (Services, Calculator,
   Reviews, Blog, FAQ, Contact) and a "Book a free chat" button.
   Hamburger menu under 768px.
2. **Hero** — headline "Friendly financial planning for sunny days and rainy ones", the pitch "We help Singapore families
   sort out retirement, CPF, insurance and investing in plain English.",
   buttons "Book a free 30-min chat" and "Try the retirement calculator",
   stat chips 15+ years · 1,200+ happy clients · S$500M planned with care,
   and Sunny saying "Hi! I'm Sunny. Let's grow your savings."
3. **Services** — six cards from services.csv (summary only; NEVER the
   INTERNAL columns).
4. **Retirement calculator** — inputs: age now, retirement age, savings so
   far (not CPF), saved each month, yearly return slider (default 4%).
   Monthly compounding. A small bar chart. The note, word for word:
   "Illustration only. Assumes a steady return and fixed monthly savings, before inflation and fees. Returns are not guaranteed and this is not financial advice."
5. **How it works** — Say hello · Get your plan · Grow together.
6. **Free Money Check-up Checklist** — not on the site yet: Lab 9 adds
   it. Email and a required PDPA consent box first, then the 10 items in
   checklist-items.md as tick boxes, with a Print button.
7. **Reviews** — the six testimonials in testimonials.csv, word for word.
8. **FAQ** — the six questions in faq.md, as an accordion.
   **Blog** — the newest three articles, "View all articles" for the rest;
   Lab 8 adds the team's first article.
9. **Contact** — name, email, phone, service (from services.csv), how to
   reach you (email / phone / WhatsApp), message, and a REQUIRED consent box:
   "I agree to Horizon Wealth Planning contacting me about this enquiry and
   handling my details under the Personal Data Protection Act (PDPA)."
   No backend: show a thank-you message.
10. **Footer** — Sunny Sunday email sign-up and, word for word:
    "This website is for general information only and does not constitute financial advice. Any projections are illustrative and not guaranteed. Please speak to a qualified adviser about your own situation."

## Acceptance tests
- Calculator: age 30, retire 62, S$20,000 saved, S$800 a month, 4% →
  **S$693,138**.
- No horizontal scroll at 375px. Keyboard focus visible. Every image has
  alt text. Contact form refuses to submit without consent.
