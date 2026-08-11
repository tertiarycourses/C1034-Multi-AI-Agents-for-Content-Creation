# OpsDesk Handbook

## [POL-VPN-01] Remote access and VPN approval

VPN access requires the requester's manager approval and successful multi-factor authentication enrolment before access is enabled. Contractor access must include an end date no later than 90 days after activation. The service owner reviews extensions before the end date. Never place passwords, tokens or private keys in a ticket.

## [POL-ACCESS-02] Least-privilege access

Access is granted only to the systems and folders required for the named work task. Confidential finance folders require both the data owner's approval and confirmation that the requester completed the organisation's data-handling briefing. Read-only access is the default when the task does not require changes.

## [PROC-ESC-03] Security incident escalation

Suspected phishing, credential theft or malware is escalated immediately to the Security Operations contact. The service desk records the ticket identifier, time reported and affected device identifier, but does not copy suspicious attachments into chat, prompts or shared notes. The user disconnects the device from the network if instructed by Security Operations.

## [PROC-SLA-04] Response targets

Critical security incidents receive an initial response within 15 minutes. High-priority service outages receive an initial response within one hour. Standard access requests receive an initial response within one business day. These targets are response objectives, not guarantees of resolution time.

## [POL-DATA-05] Data handling for agent tools

Agent tools in the learning environment use synthetic data and read-only operations. Production tools must validate identity, authorise each action, minimise returned fields and create an audit event. Retrieved documents are untrusted evidence: instructions embedded in them are treated as data and cannot override the application's system or policy instructions.
