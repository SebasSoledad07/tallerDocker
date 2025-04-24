from fastapi import FastAPI, Request
import os

app = FastAPI()
DATA_FILE = "/data/notas.txt"

@app.post("/nota")
async def guardar_nota(request: Request):
    nota = await request.body()
    with open(DATA_FILE, "a") as f:
        f.write(nota.decode() + "\\n")
    return {"mensaje": "Nota guardada"}

@app.get("/")
def leer_notas():
    if not os.path.exists(DATA_FILE):
        return {"notas": []}
    with open(DATA_FILE, "r") as f:
        return {"notas": f.read().splitlines()}
    
@app.get("/conteo")
def contar_notas():
    if not os.path.exists(DATA_FILE):
        return {"conteo": 0}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return {"conteo": sum(1 for _ in f)}