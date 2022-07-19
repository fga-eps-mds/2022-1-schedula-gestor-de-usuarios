from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"APP": "Gestor de usuários is running"}
