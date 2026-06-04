# Day 8: Code Structure & First Unit Tests

## What I Built
I refactored the entire codebase into an enterprise-grade directory structure using `APIRouter`. I also wrote my first automated unit tests using `pytest` and `TestClient`.

## What I Learned
* **APIRouter:** It feels like building LEGO blocks. You build the Snippet API in complete isolation, and then just snap it onto the main application. 
* **The Value of Testing:** Writing tests for the 422 (Bad Payload) and 404 (Not Found) errors gave me confidence. If I ever accidentally delete the Pydantic validation rules, these tests will fail immediately and warn me before the code reaches production.

## What Confused Me
When I first tried to run the app after moving the files, Python threw `ModuleNotFoundError` left and right.

## How I Solved It
I realized that Python relies heavily on execution context. Moving `main.py` into `app/` meant I had to change my startup command to `uvicorn app.main:app` and prefix my internal imports with `app.`. Using `PYTHONPATH=.` taught me how environment variables dictate Python's module resolution.

## My Analogy
A monolithic `main.py` is like running an entire company out of a single room. It works when it's just you. `APIRouter` is like building separate departments (HR, Sales, Engineering). `main.py` becomes the CEO who just manages the departments, rather than doing all the work themselves.