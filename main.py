from fastapi import FastAPI

from database import engine, Base
from src.api.routes import auth_router

app = FastAPI()

app.include_router(auth_router)
@app.on_event("startup")
async def startup():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("Database connection established")
    except Exception as e:
        print(f"Database connection failed: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
