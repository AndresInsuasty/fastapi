from fastapi import FastAPI

app = FastAPI()

@app.get("/{nombre}/{apellido}")
async def root(nombre: str, apellido: str):
    return {"message": "Hello World, it is an example!!"+nombre+', ' + apellido}
