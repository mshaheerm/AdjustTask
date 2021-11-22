from fastapi import FastAPI
from db.database import Base
from endpoints.datasets import api_router
from db.database import engine


app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(api_router)
