from fastapi import FastAPI

app = FastAPI()

print("Starting server")

@app.get("/")
async def root():
    return {"message": "Hello World"}