from fastapi import FastAPI

import Route

app = FastAPI()

app.include_router(Route.router)
