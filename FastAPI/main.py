from fastapi import FastAPI
from routes.spaceship import router as spaceship_router

# Create a FastAPI instance
app = FastAPI()

# Include the router from the spaceship module
app.include_router(spaceship_router)

# Main entry point
if __name__ == "__main__":
    import uvicorn

    """
    Start the Uvicorn server.

    The argument "main:app" tells Uvicorn where it can find an application instance,
    i.e., in the main module and the app variable.

    The host "0.0.0.0" makes the server accessible from any other computer (not just localhost).
    The port 8080 is the port where the application will be accessible.
    """
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
