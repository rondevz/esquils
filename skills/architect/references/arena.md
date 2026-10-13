# Compare architectural options

Start with the current shape and the smallest coherent change. A full arena is useful when genuinely different responsibility or contract choices remain, especially with costly migrations, security or ownership changes, concurrency, or broad consumer impact. Do not manufacture alternatives to justify an exercise.

## Shared brief

Give every comparison the same problem, affected journeys, inspected revision, facts and evidence limits, accepted meanings, selected technology constraints, protected behavior, scope bound, and verification needs. Keep product truth constant so alternatives differ in architecture rather than invented requirements.

For each viable shape, show:

- one realistic caller operation and one meaningful failure;
- owners, public contracts, data and control flow;
- rules and complexity hidden behind each interface;
- consequences for existing consumers, migration, and operational behavior;
- a faithful verification path and remaining uncertainty.

Apply the [design-quality criteria](design-quality.md). Prefer a shape whose responsibility ownership and interfaces contain relevant complexity without combining unrelated concerns into one large owner.

## Choose the depth

For a pattern-following change with adequate evidence, explain why the established shape fits and proceed to agreement without an arena. For a bounded open decision, compare the recommendation with the strongest materially different alternative directly.

For consequential uncertainty, use independent proposals and a fresh comparison when delegation is available and authorized. Give candidates the same brief and separate exploration space; require meaningful structural differences. A reviewer who authored none of the candidates compares evidence, caller usability, invariants, failure ownership, migration cost, and likely change propagation.

If independent evaluation is unavailable, provide a clearly labeled single-agent comparison. If independence was an explicit requirement, report the missing capability instead of claiming that requirement was met. Never describe your own second pass as an independent review.

## Synthesize for the user

Recommend one coherent shape and explain why alternatives lost, what costs it accepts, and what remains uncertain. Graft ideas only when their responsibilities and contracts fit together. Choose based on evidence and consequences, not majority vote or the most persuasive prose.

Stop investigation at the agreed bound. Missing facts that could reverse the decision remain blocking evidence gaps. Return the recommendation to the interactive architecture discussion; the comparison does not authorize implementation.
