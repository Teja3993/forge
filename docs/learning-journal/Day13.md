# Day 13: Wiring the UI & useEffect

## What I Built
I connected the read operations. The UI now loads the database history on mount, and dynamically updates the sidebar immediately after a successful code execution.

## What I Learned
* **The Dependency Array:** `useEffect` is powerful but dangerous. Understanding that `[]` means "on mount" and `[code]` means "run whenever the code state changes" is fundamental to React.
* **The `key` Prop:** I learned that React is lazy (in a good way). It doesn't want to re-draw the whole list. The `key` prop tells React exactly which specific `div` changed so it can update the DOM.


## My Analogy
`useEffect` with an empty dependency array is like setting up a recurring order on Amazon, but telling them to only deliver the very first day you move into a new house. It happens once upon arrival, and never again.