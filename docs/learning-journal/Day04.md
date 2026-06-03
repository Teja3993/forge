# Day 4: FastAPI & The DTO Pattern

## What I Built
* Initialized the FastAPI application (`main.py`) with a root health-check endpoint.
* Configured Uvicorn as the ASGI server to run the application.
* Designed the Pydantic schemas (`schemas.py`) to handle incoming user data (`SnippetCreate`) and outgoing API responses (`SnippetResponse`).

## What I Learned
* **WSGI vs ASGI:** Traditional Python servers (like standard Flask/Django) use WSGI and are synchronous, blocking the thread while waiting for a database response. FastAPI uses Uvicorn, an ASGI server, which utilizes Python's `async/await` event loop to handle thousands of concurrent requests without blocking.
* **The ConfigDict:** In Pydantic V2, adding `model_config = ConfigDict(from_attributes=True)` to a response schema is mandatory when working with SQLAlchemy. It tells Pydantic that the data it is reading isn't a standard Python dictionary, but an ORM object (reading `snippet.title` instead of `snippet["title"]`).

## What Confused Me
At first, it felt incredibly redundant to create a `Snippet` class in SQLAlchemy, and then immediately create a `SnippetBase`, `SnippetCreate`, and `SnippetResponse` class in Pydantic that hold the exact same variables. It felt like a violation of the DRY (Don't Repeat Yourself) principle.

## How I Solved It
I realized that DRY applies to *logic*, not necessarily to *boundaries*. The API boundary and the Database boundary are two completely different systems. By using inheritance in Pydantic (putting the shared fields in `SnippetBase`), I minimized the repetition while keeping the security benefits of the DTO pattern.

## My Analogy
The SQLAlchemy Model is the **Vault** inside a bank. The Pydantic Schema is the **Bank Teller** at the front window. 
You never let people from the street (the internet) walk directly into the vault. They must hand a deposit slip (JSON) to the Teller (Pydantic). The Teller strictly validates the slip, ensures there's no malicious intent, formats it perfectly, and *then* hands it to the vault manager to be stored safely.

## What I Still Don't Understand
Right now, the API is running, and the Database is running, but they aren't talking to each other. I still need to figure out how to safely open a database session *inside* a FastAPI route without leaving the connection hanging open forever.