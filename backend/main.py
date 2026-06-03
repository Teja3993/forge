from fastapi import FastAPI

# Initialize the FastAPI application
app = FastAPI(
    title="Forge API",
    description="The backend engine for the Forge engineering workspace.",
    version="1.0.0"
)

# A basic health-check route to ensure the server is alive
@app.get("/")
async def root():
    return {"status": "ok", "message": "Welcome to the Forge API"}

# Will add the actual Snippet routes tomorrow on Day 5!