from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import Route

app = FastAPI()
origins = [
    "*"
]
app.add_middleware(
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)
app.include_router(Route.router)
