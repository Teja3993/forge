# ADR 018: Client-Side Data Fetching via useEffect

## Context
The UI must retrieve historical code snippets from the database and keep the sidebar synchronized when new snippets are created.

## Decision
Implemented a client-side fetch using the `useEffect` hook with an empty dependency array `[]` to load initial data on component mount. Established a `fetchHistory` helper function that is recalled inside the `handleRunClick` execution block to synchronize the state after a mutation.

## Consequences
1. The UI remains decoupled from the server rendered HTML, operating as an SPA (Single Page Application) for this specific interaction.
2. Strictly relied on database UUIDs as React `key` props to guarantee stable DOM rendering during list updates.