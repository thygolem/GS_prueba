from fastapi import FastAPI
from routes.fridge import fridge

app = FastAPI()

app.include_router(fridge)
