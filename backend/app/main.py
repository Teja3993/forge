from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routers import snippets
from app.logger import logger
import time

# Initialize the FastAPI application
app = FastAPI(
    title="Forge API",
    description="The backend engine for the Forge engineering workspace.",
    version="1.0.0"
)
# --- NEW: CORS CONFIGURATION ---
# Define the exact URLs that are allowed to talk to our API.
# Do NOT use ["*"] in production, as it allows any website in the world to make requests.
origins = [
    "http://localhost:3000",  # Our future React frontend
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allow GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"], # Allow all headers (like Authorization and Content-Type)
)


# 1. THE MIDDLEWARE: Intercepts EVERY request to log it
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    # Log the incoming request
    logger.info(f"Incoming request: {request.method} {request.url.path}")
    
    # Process the request
    response = await call_next(request)
    
    # Log the completion and how long it took
    process_time = (time.time() - start_time) * 1000
    logger.info(f"Completed {request.method} {request.url.path} - Status: {response.status_code} - {process_time:.2f}ms")
    
    return response


# A basic health-check route to ensure the server is alive
@app.get("/")
async def root():
    return {"status": "ok", "message": "Welcome to the Forge API"}

# Moved below code to router/snippets.py 
# @app.post("/snippets/", response_model=SnippetResponse)
# def create_snippet(snippet_in: SnippetCreate, db: Session = Depends(get_db)):
#     try:
#         new_snippet = Snippet(
#             user_id=snippet_in.user_id,
#             title=snippet_in.title,
#             language=snippet_in.language,
#             code=snippet_in.code
#         )
#         db.add(new_snippet)
#         db.commit()
#         db.refresh(new_snippet)
        
#         # Log success!
#         logger.info(f"Successfully created snippet with ID: {new_snippet.id}")
#         return new_snippet
#     except Exception as e:
#         # Log the exact error traceback if the database fails
#         logger.error(f"Failed to create snippet: {str(e)}", exc_info=True)
#         raise HTTPException(status_code=500, detail="Internal Server Error")
    
# Moved to router/snippets.py 
# GET ALL SNIPPETS
# response_model is List[SnippetResponse] 
# @app.get("/snippets/", response_model=List[SnippetResponse])
# def get_all_snippets(db: Session = Depends(get_db)):
#     # .all() fetches every row in the table
#     snippets = db.query(Snippet).all()
#     return snippets

# Moved to router/snippets.py 
# # 4. GET A SINGLE SNIPPET BY ID
# @app.get("/snippets/{snippet_id}", response_model=SnippetResponse)
# def get_snippet(snippet_id: UUID, db: Session = Depends(get_db)):
#     # .filter() adds a WHERE clause to the SQL query. .first() returns the first match or None.
#     snippet = db.query(Snippet).filter(Snippet.id == snippet_id).first()
    
#     if not snippet:
#         logger.warning(f"Snippet lookup failed. ID not found: {snippet_id}")
#         # This throws a clean 404 error back to the user, stopping execution
#         raise HTTPException(status_code=404, detail="Snippet not found")
        
#     return snippet

# Mounting the router!
app.include_router(snippets.router)