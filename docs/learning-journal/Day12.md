# Day 12: Network Fetching & Promises

## What I Built
I connected the frontend to the backend. I wrote an asynchronous function that takes the React state, serializes it into a JSON payload, and POSTs it to the FastAPI `/snippets/` route.

## What I Learned
* **Asynchronous Javascript:** I learned how `async/await` stops the browser from freezing while waiting for a server to respond. 
* **The Fetch Trap:** I learned that `fetch` does not automatically throw an error if the server returns a 500 status. It only throws an error if the server is completely unreachable. Checking `response.ok` is mandatory.


## My Analogy
A Promise is like ordering food at a restaurant. You place the order (`fetch`), and the cashier gives you a buzzer (a `Promise`). You don't freeze and wait at the counter; you go sit down and talk to your friends (the rest of the app continues running). When the food is ready, the buzzer goes off (`await`), and you finally process the result (`response.json()`).