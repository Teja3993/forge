# Day 7: Postman & API Validation Testing

## What I Built
Today I configured CORS to prepare the backend for React, and I established an API testing workspace in Postman to systematically test the boundaries of the endpoints.

## What I Learned
* **CORS is a Browser Thing:** I understand that CORS errors aren't the server crashing; it's the browser acting as a bodyguard.
* **Pydantic is Magic:** Spent time sending broken JSON (missing fields, wrong data types) to API via Postman. Didn't have to write a single `if language is None:` check in Python route. Pydantic intercepted the bad data and returned  `422 Unprocessable Content` error automatically.

## My Analogy
CORS is like a bouncer at an exclusive club (your API). 
When a browser (like Chrome) brings a guest (a web request) from an unknown neighborhood (Port 3000), the bouncer stops them. The browser says, "Hold on, let me ask the boss." (The preflight `OPTIONS` request). The boss (FastAPI) checks the VIP list (`allow_origins`), sees Port 3000, and tells the bouncer to let them in. 

Postman, however, is like a helicopter that just lands directly on the roof of the club. It bypasses the bouncer (the browser) entirely.