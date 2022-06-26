from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import Route

app = FastAPI()
origins = [
    "http://localhost:8000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)
app.include_router(Route.router)
