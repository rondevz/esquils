# Architecture implementation brief

Keep one implementation-facing source of truth for the shared design. Use an existing architecture or feature-design document when it already owns this decision; otherwise use a user-supplied location or `docs/design/<feature-or-decision>.md` in the target project.

The brief is proportional to the change. An extension can be a small section recording reused owners and contracts; a wider decision may need several sections and a diagram. Avoid duplicating canonical vocabulary, existing ADRs, or every investigated alternative.

## Content that changes implementation

- **Identity and status:** feature or decision, inspected revision, and `Proposed`, `Agreed`, or `Blocked`. Record accepted choices and their date; distinguish facts from assumptions and recommendations.
- **Problem and scope:** required outcome, protected behavior, relevant constraints, and excluded cleanup.
- **Context and evidence:** current journeys, decisive code or runtime evidence, previous decisions, and unresolved evidence limits.
- **Caller journeys:** one normal operation and meaningful failures, including the selected interaction design and relevant states.
- **Shared shape:** responsibilities, authoritative data and state, contracts, dependencies, invariants, and failure or recovery ownership. State concrete reuse or justified structural changes.
- **Recommendation and trade-offs:** the selected option, important alternatives, costs accepted, and any independent evaluation actually performed.
- **Implementation and verification:** shared constraints tickets must preserve, local choices implementers may make, required migration sequence when applicable, agreed observable examples, and how to verify them.
- **Open questions and re-entry:** what is still unknown, what dependent work it blocks, and what new evidence would require revisiting design.

A proposal is not agreed just because the agent recommends it. User agreement already present in the conversation can be recorded without repeating an approval request. Shared choices that materially change implementation remain visible until resolved.

## Handoff and maintenance

Return the exact path and explain the agreed shape plainly. The spec and dependent tickets reference this artifact instead of maintaining competing copies. Explorer uses it to prepare the implementer's context; evidence that invalidates it returns to the affected design decision.

When a later feature changes these responsibilities or contracts, update the maintained design and its references after resolving the new decision. An ADR can preserve consequential rationale through the project's normal workflow; it is not required for every choice and is not created by this skill automatically.

Preserve the brief while dependent tickets need it. Retire a temporary brief only after its still-relevant contracts, vocabulary, rationale, and verification obligations have maintained owners in code, tests, and documentation. Record the intended lifecycle and preserve selected prototype references until their comparisons are complete. Do not perform retirement during architecture design.
