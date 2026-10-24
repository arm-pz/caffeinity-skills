# Asset structures

The skeleton per conversion asset, what each section has to do, and what to measure once it is
live. Slots in `[brackets]` mean the user must supply the content; never fill one with a guess.

## Contents

- Long-form sales page
- Landing page (paid traffic)
- Launch email sequence
- Abandoned-cart and checkout-recovery emails
- Upsell and post-purchase flow
- Ad variations: Facebook, Google, LinkedIn
- Product descriptions
- VSL script
- Webinar presentation
- Testimonial framework
- What to measure, and the first test

## Long-form sales page

Section order, and the job of each:

1. **Pre-head** (optional): names the reader so the wrong ones leave early. Cheap, and it earns the
   headline's specificity.
2. **Headline**: the single most important claim you can substantiate, in the buyer's words.
3. **Subheadline**: who it is for, by what mechanism, with what constraint removed.
4. **Lead**: the first screen of body. Do not sell yet; prove you understand the problem in detail
   only an insider would know. This is where an awareness mismatch shows up first.
5. **Problem and cost of it**: what happens if nothing changes, stated without invention.
6. **Mechanism**: why the usual approach falls short and what is different here. Name the method if
   the user has a name for it; otherwise leave `[mechanism name — supply this]`.
7. **Product introduction**: what it is, format, delivery, what the buyer holds on day one.
8. **Benefit blocks**: outcome, then how the product produces it, then the proof slot. Three to six
   blocks, no filler variations of the same benefit.
9. **Proof stack**: `[customer name]` quotes the user supplied, demonstrations, screenshots,
   numbers with a source, credentials. Each item gets a line explaining what it proves, since an
   unexplained number does no work.
10. **Offer build**: what is included, what it is worth in the user's own words, what is not
    included. Price appears here, exactly as supplied.
11. **Guarantee / risk reversal**: the user's real terms, or
    `[guarantee terms — supply this]`. Do not invent a policy and do not soften a real one into an
    adjective.
12. **Scarcity or deadline**: only if true and supplied. A fake counter is a trust and platform
    problem, not a copy trick.
13. **Close**: restate the choice in one paragraph and ask for the action.
14. **FAQ**: objections in the buyer's words, answered in the buyer's words. Write these before the
    body when the objection list is thin.
15. **PS block** (long pages): the summary for the reader who scrolled to the bottom.

CTA appears after the offer build, after the guarantee and at the close, with the same button label
each time. Changing the label changes what you are measuring.

## Landing page (paid traffic)

The message must match the ad that paid for the click, in wording and in the promise. A page with
more than one goal loses the plot; ask which action it is before writing.

Order: headline echoing the ad, subheadline, one visual of the product or outcome, the three
benefits that made the click worthwhile, proof, form or button, the terms (price, refund, delivery)
in plain text, and a short FAQ answering the objection that stops the form submit.

Diagnosing a page that does not convert, in this order:

1. Does the headline match the traffic's awareness and the ad's promise?
2. Is the CTA a single unambiguous action, visible without scrolling?
3. Is the ask (form fields, price, time) larger than the value shown so far?
4. Is there any proof adjacent to the moment of risk?
5. Is the load path buried under sections the buyer never reaches?

Name the section the friction sits in, propose the one change to test, and write it. Do not rewrite
the whole page and call it a fix; that is how a team learns nothing.

## Launch email sequence

Beats, not a fixed count. Use the beats the offer needs; the sequence length is the user's
decision and depends on list size and access.

| Beat | Job | One-line shape |
| --- | --- | --- |
| Advance notice | Wake the list without asking for money. | "On [date] I am opening [thing]. Here is why it exists." |
| Problem | Say the problem better than they can. | "The part nobody mentions about [problem] is [detail]." |
| Story / reason | Why this, why now, what changed. | "I tried [route], it failed because [cause], so I built [mechanism]." |
| Reveal | What it is, plainly, with the format and delivery facts. | "[Name] is [format] that [outcome] for [buyer]." |
| Proof | Supplied results, in the customer's words. | "[customer name]: '<verbatim quote>'" |
| Offer and price | Everything included, the number, the terms. | "[price]. You get [list]. [guarantee terms]." |
| Objection | Answer the one that stops the purchase. | "If you are thinking [objection], here is the honest answer." |
| Deadline | True urgency only, with the date and what happens after. | "Closes [date] because [reason]." |
| Last call | Short, one CTA, no new claims. | "Doors close at [time]. [button label]." |

Rules that hold across the sequence: one CTA per email and it points at the same destination; the
first line of body earns the second; subject lines make a promise the body keeps and never a claim
the product cannot support; every email is readable as plain text; the story beat does not become
the pitch beat. Write preview text as a second hook, not as a repeat of the subject.

## Abandoned-cart and checkout-recovery emails

Segment by drop-off point, because the objections differ.

- **Cart, before checkout**: reminder plus the objection the page could not answer. Ask what
  stopped them if the user's flow supports a reply.
- **Checkout, before payment**: friction reduction. Restate price, shipping, tax, delivery time and
  refund terms; repeat the guarantee next to the payment button; offer a way to ask a human.
- **Payment failed**: never accusatory, never implying the buyer is at fault. Direct link back, the
  reason in plain language, an alternative payment route, and a support contact slot.
- **Post-window value email**: the useful thing they were buying anyway, then the link back. Only if
  the product has a free slice to offer.

Timing placeholders the user must set: `[first send delay]`, `[second send delay]`, `[final send]`.
Discount-as-recovery is a pricing decision, so flag it for `strategy-memo` rather than choosing it
in copy; if the user has already decided, name the terms and the expiry exactly.

Sequence shape: subject line, preview text, the one thing they were missing, one CTA, the terms,
the guarantee, opt-out respected in every variant.

## Upsell and post-purchase flow

The buyer has already said yes, so the frame is completion, not persuasion from scratch.

1. **Thank-you / confirmation page**: confirm the purchase, say what happens next and when, then
   introduce the second offer as the thing that makes the first work fully.
2. **Upsell page**: one idea, in this order: what they just got, the gap that still exists, the
   add-on as the filler of that gap, the price difference stated honestly, the one CTA.
3. **Downsell or fallback**: the smaller version, or the payment-plan route if the user offers one.
   Never imply the buyer cannot afford something; offer the cheaper path without commentary.
4. **Bumps and order bumps**: two or three sentences next to the checkout form, describing the
   add-on's outcome and its price. No new claims.
5. **Confirmation email**: receipt facts, delivery instructions, support route, and the add-on again
   for anyone who missed it, clearly marked as optional.
6. **Onboarding email**: how to start, so the refund and chargeback rate stays low. The single most
   underrated conversion asset.

Do not claim the add-on is required for the main product to work unless the user says it is.

## Ad variations

Build a grid, then write each cell. Angles down one axis, form along the other:

| | Short hook | Medium hook | Long hook |
| --- | --- | --- | --- |
| Problem-direct | one-line pain | pain plus cost | pain plus failed attempts |
| Outcome-first | result claim | result plus timeframe the user supplied | result plus who it worked for |
| Mechanism / curiosity | why the usual route fails | the different method named | the method plus the objection it removes |
| Social proof | supplied quote fragment | supplied number with source | story of one named customer the user supplied |
| Objection / myth | "no [thing]" | myth plus correction | myth, correction, proof |
| Price or offer | the number | number plus what is included | number plus terms and expiry |

Then per variant: hook line, body, CTA label, and a note on what the creative or first frame has to
carry, since the image does a share of the work.

Per-platform constraints, to check against current docs before launching rather than trusting this
file:

- **Meta (Facebook and Instagram)**: main text, headline and description all truncate, and the
  displayed amount depends on placement. Write the hook in the first clause. Avoid the
  personal-attribute pattern (asserting the reader's age, health, finances, employment or that they
  are failing at something); platforms commonly reject it, so write the attribute as a general
  statement about the market. Do not imply inside knowledge of the reader.
- **Google Search**: headline slots, description slots and character limits per ad type. Put the
  query's words in the headline so relevance is visible to the searcher. One feature per description
  slot; write more variants than the minimum so the format can be tested.
- **Google Display / YouTube**: the visual carries the promise, so the copy is one claim plus one
  instruction.
- **LinkedIn**: professional framing, no fabricated personalisation, and the hook is the first two
  lines before the truncation. Write as one practitioner to another.

Never write an ad that promises a result the landing page does not restate. The mismatch is where
money leaks.

## Product descriptions

Three lengths, same facts:

- **Short (category / feed)**: one sentence, outcome plus the defining spec, no superlatives.
- **Long (PDP)**: opening hook, who it is for, three benefit blocks (outcome, how, with what),
  specifications exactly as supplied, what is in the box, care or compatibility limits, the one CTA.
- **Field set**: title pattern, bullets for scan, alt-text suggestion, and the metadata the user's
  store needs.

Keep every spec, material, dimension, compatibility and certification string exactly as the user
wrote it. "Benefit-driven" applies to the framing, never to the facts: a benefit invented to sell a
product is a returns and liability problem.

## VSL script

Time-coded, written to be read aloud by one voice:

1. **Pattern interrupt**: a statement that does not match what the viewer expected, no logo roll.
2. **Identify and problem**: who this is for, and the problem described in insider detail.
3. **Agitate honestly**: the cost of staying, drawn from what the user reported, not from a
   fabricated worst case.
4. **Failed alternatives**: what they have tried and the structural reason each fell short.
5. **Mechanism reveal**: why this approach differs. Teach enough that the claim is earned.
6. **Proof**: supplied results, demonstrations, named customers only as the user supplied them.
7. **Offer stack**: what is included, in the order the buyer feels the value.
8. **Price justification**: comparison the user supplied, or the cost of the problem, never an
   invented anchor.
9. **Guarantee**: stated terms, plainly, with the conditions intact.
10. **Direct close**: instruct the viewer exactly what to click and what happens next.
11. **Second close**: restate the choice for viewers who are still watching.

Retention beats are a craft choice, not a promise: open loops, one idea per sentence, no sentence
that cannot be said without breathing. Mark every place the video must show something with
`[on-screen: ...]`.

## Webinar presentation

Run sheet with timings that sum to the slot the user booked.

- **Framing and promise**: what they will be able to do by the end, and the ground rules.
- **Teaching blocks**: three to five, each with a takeaway the attendee can act on, since a webinar
  that teaches nothing gets refunds. Keep the real method teachable and the implementation paid.
- **Proof woven through**: examples the user supplied, at the moment each claim needs backing.
- **Transition**: name the gap between what they now know and what they want done, then introduce
  the offer as the way to close it.
- **Offer stack and price**: as the sales page, but spoken, with the terms restated twice.
- **Guarantee**: the real policy, read exactly.
- **Close and Q&A**: a hard close first, then answers, then one final close. Write the answers to
  the objections the user has actually heard, and slot the rest as `[objection — supply this]`.

For a sixty-minute slot, hold the pitch back until the teaching has paid for the attention, but do
not claim attendees convert "before the pitch"; the honest mechanism is that the teaching makes the
pitch relevant.

## Testimonial framework

**The rule, stated where the framework lives: this skill never writes a testimonial.** It does not
compose a plausible quote, a name, a job title, a location, a rating, a photo credit or a result.
An invented testimonial is a fabricated claim about a person who does not exist, it is unlawful in
most markets, and it destroys a brand when found. If a quote is needed and none exists, the answer
is to go and get one, using the questions below.

Ask the customer these, in one conversation, and record their answers verbatim:

1. What was happening that made you look for a solution?
2. What did you try before this, and what went wrong with it?
3. What almost stopped you from buying?
4. What made you decide?
5. What changed, in numbers or in a sentence a colleague would notice?
6. Who else should buy this, and who should not?
7. Which one sentence from you would you want a stranger to read?

Then check: written permission to use it, the form of name attribution allowed, whether the result
is typical or needs the qualifying line, and whether the platform the quote will appear on has
extra rules about it.

Structure to fill once the answers exist:

```
"[verbatim quote, result-first or objection-first]"
[customer name — supplied] · [context: role, company, situation — supplied]
Result: [before] -> [after], [metric — supplied], measured [timeframe — supplied]
Used with permission: [yes/no — confirm]
```

Three shapes, in the same no-fabrication frame:

- **Objection-killer**: the customer who almost did not buy, in their words, placed next to the
  objection it answers.
- **Specific-result**: one number, one timeframe, one named person, placed beside the claim it
  substantiates.
- **Transformation arc**: before state, decision point, after state; the longest of the three and
  the one that needs the most permission checks.

Where no real customer exists yet, output the framework and the questions, and write
`[proof — no testimonial available. Do not substitute one.]` in the proof stack. A slot is a valid
deliverable; a made-up quote is not.

## What to measure, and the first test

Replace "conversion-optimised" with a measurement plan the user can run.

- **Sales page and landing page**: sessions, conversion rate to the primary action, scroll depth to
  the offer, and the source split. A page and a form are different denominators; say which you mean.
- **Emails**: delivery first, then opens as a weak interest signal, then clicks to the destination,
  then revenue per recipient. List growth and unsubscribes belong in the same table.
- **Ads**: hook rate or thumb-stop as reported by the platform, then click-through, then cost per
  lead, then cost per purchase by placement. Stop at the metric you can act on.
- **VSL**: watch time at the offer reveal relative to starts, and click-through from the button
  frame.
- **Webinar**: registration-to-attendance, attendance-to-offer-page, offer-page conversion.
- **Upsell**: take rate, refund rate on the main product, revenue per buyer overall.
- **Cart recovery**: recovery rate per drop-off segment, counted separately from the flow that
  offered a discount.

A reasonable first test: change one thing, on one asset, for one audience segment, and pre-register
what you expect to happen and why. Write it as
"headline angle: template-versus-specific. Expect more qualified clicks; measure booked calls per
session. Run until `[minimum sample — supply this]` or `[end date]`."

Baseline and significance are the user's data or nobody's claim. Sample-size maths belongs to
`data-readout`; if the traffic is too small to learn from, say so before spending on the test and
suggest changing the offer or the traffic instead.
