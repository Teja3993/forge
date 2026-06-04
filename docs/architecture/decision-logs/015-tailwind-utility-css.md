# ADR 015: Tailwind CSS for Styling

## Context
Writing custom CSS or using preprocessors like SASS leads to large stylesheet bundles, "dead CSS" (styles that are no longer used but developers are afraid to delete), and naming collisions (BEM methodology). 

## Decision
Utilize Tailwind CSS, a utility-first CSS framework.

## Consequences
1. **Zero Dead CSS:** Tailwind scans the React components at build time and only ships the CSS classes that are actively written in the code.
2. **Rapid Prototyping:** Developers do not need to switch context between `.tsx` files and `.css` files.
3. **Consistency:** Using predefined classes like `p-4` or `bg-gray-900` enforces a strict design token system without needing a dedicated UX designer.