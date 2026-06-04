# ADR 014: Next.js App Router for Frontend


## Context
We need a framework to build the React user interface. Using raw `create-react-app` is deprecated by the React core team and suffers from Client-Side Rendering performance issues. A system is needed that supports strict typing to match the safety of our Pydantic backend.

## Decision
Adopted Next.js 14+ (v16.2.7) utilizing the new App Router paradigm, strictly enforcing TypeScript, and using Tailwind CSS for atomic utility styling.

## Consequences
1. Components default to Server Components, reducing the client-side JavaScript bundle size.
2. File-based routing (folders acting as URL paths) simplifies navigation architecture.
3. Strict TypeScript compilation will force us to define explicit interfaces for the data fetched from the FastAPI backend.