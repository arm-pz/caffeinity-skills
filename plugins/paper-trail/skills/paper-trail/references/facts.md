# Fact sheet

Copy this to `facts.md` next to the drafts and fill it with the owner. One line per fact,
`key: value`. The checker reads these lines: emails, URLs and the company name in the pages must
appear here. Leave an unknown value as `[NEEDS: ...]`, never a guess. Mark values you read from
the site or code with `(observed)` until the owner confirms them.

Required entries are marked `*`.

## Who

- legal_name*: the person or company that runs the product
- trading_name: the name users see, if different
- product_name*:
- product_url*:
- contact_email*: where users send privacy and refund requests
- postal_address: required in the EU/UK and for some US states; ask
- countries_operated_from*:
- countries_of_users*: "worldwide" is an answer; so is "India and the US"
- minimum_user_age*: 13, 16, 18; under 16 is an escalation trigger

## Data

- data_collected*: each item and where it comes from (sign-up form, checkout, analytics, uploads)
- purpose_of_each*: why each item is collected; one purpose per item
- legal_basis: EU/UK only (contract, consent, legitimate interest)
- processors*: every third party that receives data, with what it gets
  (payment, email, analytics, hosting, error tracking, fonts, embeds)
- data_sold_or_shared_for_ads*: yes or no; yes is an escalation trigger
- retention*: how long each item is kept, or the rule that decides it
- storage_location: country or region of the main host
- security_summary: one honest sentence (for example "encrypted in transit; access limited to the owner")
- user_rights_process*: how a user asks to see, correct, export or delete their data, and the reply time

## Cookies

- cookies_essential: name and purpose
- cookies_non_essential: analytics, ads, embeds; any entry here needs a cookie notice
- consent_tool: the banner or tool, if any

## Money

- charges*: free, one-time, subscription or usage-based, and the prices or where they are shown
- payment_provider:
- billing_cycle_and_renewal: and how to cancel
- refund_window: days, or "no refunds" with any statutory exception
- refund_conditions:
- taxes: who collects (merchant of record or the owner)

## Terms

- what_the_product_does*: one sentence
- acceptable_use: what users may not do
- user_content: whether users upload content, who owns it, and the licence the product needs
- account_termination: when the owner may close an account
- liability_cap: if any
- governing_law*: the country or state whose law applies
- disputes: courts or arbitration
- effective_date*: the date these pages take effect
- changes_notice: how users hear about changes
