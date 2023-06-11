from fastapi import FastAPI
from routes.spaceship import router as spaceship_router

app = FastAPI()

app.include_router(spaceship_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8080)
