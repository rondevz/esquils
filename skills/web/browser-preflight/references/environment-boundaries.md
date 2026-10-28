# Environment boundaries

Use the branch that matches the observed failure. Commands and runtime APIs come from the current project and installed tools; names and ports below are illustrative.

## Container dependency fails

A database can be healthy while disconnected from the app's Compose network. For an error such as `could not translate host name "pgsql"`, inspect the app and database network membership, service alias, and name resolution from the app container. Distinguish a missing network attachment from a stopped service, credentials, or schema failure.

Repair the demonstrated mismatch using the project's existing network configuration, then repeat the dynamic request. Recreating the whole stack or removing volumes is not a DNS diagnostic. Retain data and user-owned services; confirm that the repair also agrees with the configuration used at the next launch.

For fixtures, identify the database instance as well as the database name. Separate Compose projects can each contain a database named `testing`; the name alone does not prove which instance receives mutations. Confirm effective runtime configuration in the web process and setup process, because caches and launch wrappers can change which settings they use.

## Agent and browser see different networks

`localhost` names the network context of the caller. Compare the dynamic request inside the app container, from the agent's shell, and from the browser. A Docker port binding, host-network container, or shell listener can exist without being reachable from the other contexts.

Use a harness-provided environment-port target or an established project forwarding path when available. Retry only when a probe identifies a changed boundary. If an installed alternative browser is permitted after native-preview failures, use it with the same isolated application and document the executor change.

A temporary relay over an existing container-exec transport can bridge a confirmed namespace mismatch when a maintained helper already exists. Keep its lifecycle bounded to the run, verify the target service and database, and preserve ordinary HTTP, assets, sessions, and CSRF behavior. Building such a relay and browser controller from scratch is a separate environment task, not the default acceptance fallback.

## Browser session or ownership fails

Check the tool's session status and ownership before acting. When the native preview is initially unavailable, try its documented initialization once before declaring it absent. Use the returned tab handle for subsequent calls, especially when multiple tabs exist.

A message such as `The calling provider no longer owns an active thread run` describes orchestration ownership, not application health. Hand the browser step to an active authorized session once and pass its known URL and fixture. Respect human-controlled tabs and the selected browser profile.

## Page loads but assets or interactions are wrong

Check the expected app identity, entry scripts, stylesheet completion, and visible starting state before taking evidence. An empty root or an unstyled page is not a valid visual comparison. Wait for an observable ready condition rather than an arbitrary sleep.

A build can invalidate assets already loaded by an open tab. Use the executor's cache controls and reload the current build before retrying. For Vite-style stacks, a leftover development-server marker can point a fixture at an unreachable asset server. Choose a supported fixture-specific asset configuration while preserving the user's development server and markers.

For keyboard evidence, confirm that the executor sends the documented key sequence to the intended focused page. A malformed automation event is not a product defect. Test the semantic result: opening a control, moving focus within the dialog, closing it, and returning to the origin or a useful fallback when that origin disappears. A desktop viewport resize establishes responsive layout evidence, not physical-device or virtual-keyboard coverage.
