# Day 5: Dependency Injection & Database Integration

## What I Built
Today, I bridged the gap between the FastAPI web server and the PostgreSQL database. I wrote a dependency injection function using Python generators and created a `POST /snippets/` route that receives internet traffic, validates it via Pydantic, converts it to an ORM model, and saves it to Neon.

## What I Learned
* **Dependency Injection:** It sounds like a complex enterprise buzzword, but it simply means "do not let the function create its own tools; pass the tools *into* the function."
* **The Power of `yield`:** I learned how `yield` pauses a function. It allows FastAPI to handle the DB setup before the route runs, and the DB teardown after the route finishes.
* **Foreign Key Enforcement:** My API crashed when I tried to submit a snippet without a valid user ID. This proved that the relational constraints I wrote in raw SQL on Day 1 are actively protecting the application.

## What Confused Me
The data conversion step was initially confusing. I had to explicitly map `snippet_in.title` (from the Pydantic schema) to `title=` (in the SQLAlchemy model). I initially wondered why I couldn't just pass the JSON directly to the database.

## How I Solved It
I realized this is the DTO (Data Transfer Object) pattern in action. Manually mapping the fields is a security feature. It prevents users from injecting fields they shouldn't have access to.

## My Analogy
Dependency Injection is like checking into a hotel. 
When I (the API request) arrive at the front desk, the receptionist (FastAPI `Depends`) hands me a key to an empty room (the `yield db` session). I do whatever I need to do in that room. When I leave, the receptionist automatically takes the key back and cleans the room (`finally: db.close()`). I didn't have to build the room myself, and no other guest was allowed in my room while I was there.