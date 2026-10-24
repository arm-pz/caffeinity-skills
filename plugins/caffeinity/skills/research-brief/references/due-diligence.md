# Due diligence

For "check them before I sign, invest or hire". The deliverable is a sourced picture plus a list of open questions the counterparty must answer. It is never an approval or a veto: the recommendation belongs to `strategy-memo`, the pressure-test of a decision already taken belongs to `crash-test`.

Common rules for all three checklists:

- Every line is either a claim with a source row (see `verification.md`), a question, or `[not established in this session]`. Blank-looking honesty beats a filled-in guess.
- Anything only the counterparty can supply goes under **Ask them for**, with why it matters and what a bad answer would look like. Do not infer what they will not disclose.
- Public record is not character. Registries, filings and press tell you what happened on paper.
- Name the date of scan at the top. Diligence goes off in weeks.
- Red flags are for verified findings only. "Their website is dated" is a note; "their filing lists a director who appears in a sanctions register" is a red flag, and needs its source.
- If there is no network in the session, output `STATUS: INCONCLUSIVE` and hand over the checklists as the questions to run, with nothing answered.

---

## Partner / counterparty checklist

**Scope first:** who is "them" — the legal entity, not the brand. Two entities can share a name and a website.

Verifiable externally, each needing a dated source:

1. Legal identity: registered name, number, jurisdiction, incorporation date, whether the entity is active or struck off.
2. People: directors or principals named on the register; how long they have been there; other companies they are connected to.
3. Ownership: parent, subsidiaries, ultimate beneficial owner if disclosed; whoever the filings name.
4. Financial footprint: published accounts where the jurisdiction requires them, funding announcements, any bond, credit or insurance disclosures.
5. Track record: named customers or partners they claim, case studies, dates of those claims; whether the claimants confirm them when asked.
6. Public disputes: litigation, arbitrations, regulatory actions, sanctions or debarment lists, recall notices — in the registers that apply to that jurisdiction.
7. Dependence: whether their own site or filings show revenue concentrated on one client, one platform or one founder.
8. Continuity: domain age, staff turnover signals, changelog or posting gaps, hiring freeze or growth.
9. Security and compliance posture: certifications they claim, the issuing body, the expiry date if published. Certifications with no verifiable register go on Ask them for.
10. Reputation as reported: press, trade coverage, review platforms. Treat each as one person's claim with a date, and put disagreements in Conflicts.

Ask them for:

- Audited or management accounts, and the period they cover.
- Customer references you can contact, not names printed on a page.
- The contract entity, insurance certificates, and any subcontractors who will actually do the work.
- Their side of any dispute on the register, in writing.
- Data-processing terms, if personal data moves.

Red flags, verified only:

- Entity registered recently with the deal depending on its history.
- Named principals absent from the register you did read.
- Address shared with a large number of unrelated filings, where the register shows that.
- Claims of certifications no issuing body lists.
- Accounts that stop being filed.
- Disputes they did not disclose when asked directly, which you then find.

---

## Investment checklist

Scope: the round, the instrument, the jurisdiction. This is diligence on facts, not advice on whether to invest; the recommendation is the user's and, when they want it written, `strategy-memo`'s.

Verifiable externally:

1. Entity chain: what exactly the investor holds, in which entity, per the term sheet or filing they supply.
2. Filings and registers: annual returns, charges, cap-table statements where public.
3. Money in: dated funding announcements, amounts, lead investors named by the source that reported them, prior rounds.
4. Claims about traction: users, revenue, growth, retention. Each one either sourced to the company's own dated statement and labelled as such, or on the Ask-them-for list. Never restate a traction number as fact.
5. Market figures: the total addressable market the deck claims, checked against the rules in `report-formats.md` for industry scans. Report what the public estimates say and how they differ, and say whether the deck's definition of the market is the same as the estimate's.
6. People: founders' and executives' stated backgrounds against registries, companies' own pages, dated press, any public academic or employment record. Mark anything you could not confirm.
7. Legal exposure: litigation, IP disputes, regulatory letters, debarment, sanctions screening for the jurisdictions that apply.
8. IP: registrations they claim, with the register you checked and the date.
9. Exit history: prior companies of the same principals, what happened to them, per the sources read.
10. Related parties: investors, suppliers or customers connected to the founders, from the disclosures.

Ask them for:

- Cap table, post-money, with option pool stated.
- Term sheet, liquidation preference, anti-dilution, pro-rata rights, board composition.
- The metrics behind the traction claim, with definitions and the period.
- Customer contracts with concentration: the largest customer's share of revenue.
- Runway and burn as they calculate them, plus the assumptions.
- Any existing debt, charge or convertible instrument not in the deck.
- Cap table and shareholder agreement diffs between rounds.

Red flags, verified only:

- Numbers in the deck that no source supports and the founder will not define.
- Revenue concentrated in one customer, undisclosed.
- A market-size claim whose only citation is a report that does not exist when you search for it.
- Rounds announced publicly that no register reflects.
- Directors or shareholders who cannot be reconciled between the deck and the filings.
- Litigation disclosed to you after you found it yourself.

---

## Hire checklist

Boundary: judging a CV, resume or LinkedIn profile is `recruiter-lens`. Writing the application material is `applicant-kit`. This skill covers external verification of what a candidate or a hiring agency claims, and sourcing the market context around a role.

Verifiable externally, with care:

1. Employers and dates: only what the candidate states, plus what their own published pages or the employer's announcement say. Note the difference between "stated" and "confirmed".
2. Registrations and licences: the professional register for the field, the number, the status, the expiry.
3. Credentials: the awarding institution's own record; degree-verification services where the jurisdiction has them. Diplomas from unaccredited bodies go in Conflicts, not in the summary.
4. Published work: papers, talks, repositories, standards contributions, each with the source and date you saw it.
5. Claims of scale: "led a team of N", "owned $X of book". Only the candidate's statement unless a source confirms; label as stated.
6. Gaps and overlaps in the timeline: arithmetic on dates the candidate gave is fair game and needs no source.
7. References: named people, their published roles, whether they are former managers or peers. Contacting them is the user's action.
8. Agency and recruiter terms: fee basis, replacement-period guarantee, exclusivity, in the contract, not the email signature.

Ask them for (through the user, never directly):

- Right-to-work status and how they will evidence it, per the local rules.
- Notice period and start date, in writing.
- Compensation expectations, and any non-compete or IP assignment they are carrying.
- Verification consent for registers and prior employers, where the jurisdiction requires consent.

Note what you cannot verify, and say it plainly: employment dates at private companies, unlisted titles, and the truth of an interview answer are usually outside public record. Unverifiable is not a red flag. Put it in Gaps with the way to close it.
