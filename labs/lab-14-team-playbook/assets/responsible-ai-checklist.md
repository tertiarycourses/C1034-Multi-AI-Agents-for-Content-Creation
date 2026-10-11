# Responsible AI checklist for the studio (Lab 14)

| Area | Rule | Control in our studio |
|---|---|---|
| Human oversight | A named person approves every external piece | approvals.csv + approval typed by a person + the gate |
| Accuracy | Every figure from the facts sheet | fact-check skill; reviewer agents |
| Regulation | MAS digital advertising principles | fin-compliance skill; compliance checklist |
| Privacy (PDPA) | Marketing only to opted-in contacts; minimum personal data in prompts | recipients.csv filter; no client data in agents |
| Transparency | AI-made visuals and voices disclosed | video description line; no synthetic "clients" |
| Rights | Only images, music and fonts we may use | brand assets; licence notes |
| Security | Keys only in .env; agents never see them | .gitignore; publish.mjs masks tokens |
| Records | Keep the approved version, approver and date | approvals.csv, publish-log.csv |
| Cost | Teams cost more tokens — use them where they pay | run-log.csv review |
