from fastapi import FastAPI
from app.api.movies import movies

app = FastAPI()

app.include_router(movies)