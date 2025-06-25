from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.auth import auth_api_router
from app.api import api_router
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_api_router, prefix="/api")
app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Hello World"}
