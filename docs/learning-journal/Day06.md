# Day 6: Core Routes & Basic Backend Logging

## What I Built
I completed the read operations (GET) for the Code Snippets. I built a logging middleware that wraps the entire application, tracking every single request that hits the server.

## What I Learned
* **RESTful Error Handling:** I learned how to use `HTTPException` to throw proper 404 errors when a database lookup returns `None`. 
* **Middleware:** I learned how to intercept HTTP requests. The `call_next(request)` pattern  allows me to run code *before* the route, let the route do its job, and then run code *after* the route finishes.

## What Confused Me
I had to make sure the UUID I was searching for in the GET request actually matched the formatting expected by Postgres.

## How I Solved It
Using FastAPI's path parameter type hinting (`snippet_id: UUID`) automatically handles the validation. If a user passes a string that isn't a valid UUID, FastAPI rejects it before it even hits database query!

## My Analogy
Middleware is like the security guard at the front desk of a corporate building. 
When a visitor (HTTP Request) arrives, the guard writes down the time they entered (Start log). The visitor goes to the specific office they need (The Route). When the visitor leaves, the guard writes down the time they departed and whether their meeting was successful (End log). The office workers didn't have to track the entry/exit times themselves.