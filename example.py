from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root(nombre: str, apellido: str):
    return {"message": "Hello World, it is an example!!"}
