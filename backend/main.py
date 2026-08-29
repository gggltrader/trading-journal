from fastapi import FastAPI

from database import Base, engine
from models import Trade


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Trading Journal API",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "name": "Trading Journal API",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
    }