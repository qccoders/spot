from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api import api

app = FastAPI(docs_url=None, redoc_url=None)
app.mount("/api", api)
app.mount("/", StaticFiles(directory="/static", html=True))
