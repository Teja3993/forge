# Day 10: Static UI & Tailwind CSS

## What I Built
I constructed the visual skeleton of the application. I created a two-pane layout featuring an history sidebar and a dynamic main workspace with a text area and action buttons.

## What I Learned
* **Flexbox Geometry:** I learned the "Holy Grail" of web app layout: `<div class="flex h-screen">`. Placing a fixed-width div (`w-64`) next to a flexible div (`flex-1`) perfectly separates the navigation from the workspace.
* **Tailwind Productivity:** Once you memorize basic Tailwind prefixes (`m-` for margin, `p-` for padding, `bg-` for background), writing UI becomes incredibly fast. 

## What Confused Me
The `<textarea>` looked ugly by default. It had a white border when I clicked on it, and users could drag the corner to break the layout.

## How I Solved It
I used Tailwind utility classes specific to forms: `resize-none` removes the drag handle, `focus:outline-none` removes the ugly default blue browser glow, and `bg-transparent` allows it to blend into the parent container.

## My Analogy
Writing standard CSS is like painting a house by mixing your own custom colors in buckets; it's messy and hard to replicate the exact color twice. Tailwind is like having a predefined box of LEGO bricks. You can build anything, and because the bricks are standard sizes, everything fits together perfectly.