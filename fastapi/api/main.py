from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import auth
from api.database import Base, engine
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hallo Wereld"}

app.include_router(auth.router)