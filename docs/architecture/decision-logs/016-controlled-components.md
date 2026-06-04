# ADR 016: Controlled Components for Code Editor

## Context
The user's C++ code needs to be extracted from the UI to send it to the backend via an HTTP POST request. Using a React `ref` to read the DOM directly (Uncontrolled) or managing the text in a React state variable (Controlled), one of them must be chosen.

## Decision
Implemented a Controlled Component architecture using the `useState` hook. The `<textarea>` value is strictly bound to the `code` state variable, and every keystroke updates the state via `onChange`.

## Consequences
1. React remains the single source of truth for the application state.
2. Because state updates on every keystroke, future features can be easily implemented like live character counting, syntax validation, or WebSocket broadcasting without querying the DOM.
3. The component was converted to a Client Component using the `"use client";` directive, as Server Components do not support browser interactivity.