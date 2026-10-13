---
name: to-spec
description: "Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed."
disable-model-invocation: true
---

This skill takes the current conversation context and codebase understanding and produces a spec. Synthesize what is already known without reopening a broad interview. Resolve only missing acceptance-flow or verification details below; a change to product scope or shared architecture returns to feature design rather than being silently invented here.

The issue tracker and triage label vocabulary should have been provided to you. If not, tell the user to run `/setup-matt-pocock-skills`.

## Process

1. Explore the repo to understand the current state of the codebase, if you haven't already. Use the project's domain glossary vocabulary throughout the spec, and respect any ADRs in the area you're touching.

When architect has produced a brief, read its agreed decisions and the selected interaction-design references before synthesis. Carry shared responsibilities, contracts, protected behavior, and verification obligations into the spec with pointers to their source. A proposed or blocked shared decision remains unresolved; return it to feature design instead of publishing dependent work as ready. Do not repeat questions already settled in the architecture discussion.

2. Sketch out the seams at which you're going to test the feature. Existing seams should be preferred to new ones. Use the highest seam possible. If new seams are needed, propose them at the highest point you can. The fewer seams across the codebase, the better - the ideal number is one.

Check with the user that these seams match their expectations.

Define the acceptance flows with the user before implementation: starting state and representative data, action or sequence of actions, expected observable result, and the verification method. Reuse previously agreed examples without asking again. Cover relevant failures and visual or interaction states, not just the happy path. Mark whether each flow is a repeatable test, an agent-driven product walkthrough, or a visual comparison. Record missing execution capability separately from undecided behavior.

3. Write the spec using the template below, then publish it to the project issue tracker. Apply the `ready-for-agent` triage label - no need for additional triage.

<spec-template>

## Problem Statement

The problem that the user is facing, from the user's perspective.

## Solution

The solution to the problem, from the user's perspective.

## User Stories

A LONG, numbered list of user stories. Each user story should be in the format of:

1. As an <actor>, I want a <feature>, so that <benefit>

<user-story-example>
1. As a mobile bank customer, I want to see balance on my accounts, so that I can make better informed decisions about my spending
</user-story-example>

This list of user stories should be extremely extensive and cover all aspects of the feature.

## Implementation Decisions

A list of implementation decisions that were made. This can include:

- The modules that will be built/modified
- The interfaces of those modules that will be modified
- Technical clarifications from the developer
- Architectural decisions
- Schema changes
- API contracts
- Specific interactions

- The agreed architecture brief and selected design references, with shared constraints implementation must preserve

Avoid prescribing specific implementation file paths or code snippets; they can become outdated quickly. Exact links to governing architecture and design artifacts are context references and should be preserved.

Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it within the relevant decision and note briefly that it came from a prototype. Trim to the decision-rich parts, not a working demo, just the important bits.

## Testing Decisions

A list of testing decisions that were made. Include:

- A description of what makes a good test (only test external behavior, not implementation details)
- Which modules will be tested
- Prior art for the tests (i.e. similar types of tests in the codebase)

- Agreed acceptance flows, each with its starting state, actions, expected result, and verification method
- Selected design references and relevant states for visual comparisons
- Existing launch, data setup, and verification commands; gaps that must be resolved before required flows can be checked

## Out of Scope

A description of the things that are out of scope for this spec.

## Further Notes

Any further notes about the feature.

</spec-template>
