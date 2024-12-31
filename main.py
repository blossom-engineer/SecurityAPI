from fastapi import FastAPI
import uvicorn

from src.routers import IPA

app = FastAPI()
app.include_router(IPA.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="debug"
    )
