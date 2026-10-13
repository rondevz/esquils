---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

If the user passes a ticket reference, fetch it from the issue tracker and state its title before starting. If the reference is ambiguous, ask.

Record the initial checkout state and current HEAD when one exists, so review can distinguish this ticket's changes from pre-existing edits. For a new repository with no commits, note that review must use initial working-tree mode rather than a HEAD comparison.

Before editing, run the bundled [explorer](../../explorer/SKILL.md) for this ticket in the implementation checkout. Use its governing decisions, reuse map, affected consumers, and verification map as the implementation context. Load the local skill through the harness when possible; otherwise read its instructions and follow them directly. An explorer report is preparation, not proof that the delivered behavior works.

If the work is delegated, give the implementer the ticket, spec, agreed design and architecture references, and any inspection report. Require the implementer to run explorer in its own checkout; do not assume it inherits the parent's context. Delegation is optional and must be authorized.

Resolve blocking product or shared architecture questions before implementing dependent work. Leave local reversible choices to the implementer. Do not create a new shared design to fill an undocumented gap.

Use the acceptance flows agreed in the ticket or spec. If expected results are missing or materially ambiguous, clarify them with the user before dependent implementation; do not invent success criteria after seeing the solution.

Call the Skill tool with "tdd" where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Exercise the agreed acceptance flows against the real product using the project's existing verification tools. For UI work, drive the relevant states and compare them with the chosen design and neighboring views. Check persistence with a reload or subsequent read when required. An agent-driven walkthrough provides observed evidence; it is not automatically a repeatable test suite. Do not introduce a new testing dependency without the user's choice.

When the project's selected method is Manuvra and the runtime and harness allow it, follow the bundled [manuvra](../../manuvra/SKILL.md) skill. Use the agreed flows to author jobs, verify returned evidence, and check persistence through the application's own interface or data seam. Respect harness-specific browser-tool preferences. A missing executable or key is an execution gap, not a passing flow; do not silently install tooling or replace the selected provider.

Record which flows passed, failed, or could not run, with concrete evidence. Fix in-scope failures and rerun affected checks after the final edit. If a required flow cannot be verified, report the gap rather than marking the ticket verified or complete.

Once done, call the bundled "code-review" skill with the ticket/spec, the recorded starting HEAD as its fixed point when available, the initial checkout state, and the paths changed for this ticket. Include uncommitted changes by selecting working-tree review mode, as well as applicable committed changes; do not review only HEAD and omit the implementation waiting to be committed. For a repository without an initial commit, request initial working-tree review instead. Fix findings and rerun affected verification.

Record delivery and verification evidence in the ticket according to the project's tracker conventions and existing authorization. For a local ticket, include its delivery record in the same commit when project conventions allow; for an external tracker, report the commit and push results in the completion update. Follow the configured completion rule; pushing a branch alone does not establish integration or authorize closing a ticket whose completion requires integration.

After checks pass and review findings are resolved, commit the changes belonging to this work to the current branch and push it to its configured upstream. Do not include unrelated working-tree changes or use force push.

If the branch has no upstream, use the project's configured remote and establish tracking when the destination is unambiguous. If no remote is configured or the destination is unclear, report the missing destination instead of guessing. Report commit and push results separately; a failed push leaves delivery incomplete.

Finish the requested ticket. Do not automatically start subsequent tickets unless the user authorized a batch.
