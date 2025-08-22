from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
import json
import os

# Caminho do arquivo de persistência
DB_FILE = "tasks.json"

# -------------------------
# Modelo de dados (Pydantic)
# -------------------------

class Task(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str] = ""
    status: str = Field(default="pendente", pattern="^(pendente|concluída)$")


# -------------------------
# Funções utilitárias JSON
# -------------------------

def load_tasks() -> List[Task]:
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            return [Task(**item) for item in data]
        except json.JSONDecodeError:
            return []

def save_tasks(tasks: List[Task]):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump([t.dict() for t in tasks], f, ensure_ascii=False, indent=2)

# -------------------------
# Inicialização do FastAPI
# -------------------------

app = FastAPI(
    title="API de Tarefas",
    description="CRUD básico de tarefas usando FastAPI e JSON.",
    version="1.0.0"
)

# CORS Middleware (permite requisições de qualquer origem)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Rotas
# -------------------------

@app.get("/", summary="Home")
def home():
    return {"message": "API de Tarefas Online"}

@app.get("/tarefas", response_model=List[Task], summary="Listar tarefas")
def listar_tarefas():
    return load_tasks()

@app.post("/tarefas", response_model=Task, summary="Criar tarefa")
def criar_tarefa(tarefa: Task):
    tarefas = load_tasks()
    if any(t.id == tarefa.id for t in tarefas):
        raise HTTPException(status_code=400, detail="ID já existe.")
    tarefas.append(tarefa)
    save_tasks(tarefas)
    return tarefa

@app.put("/tarefas/{id}", response_model=Task, summary="Atualizar tarefa")
def atualizar_tarefa(id: int, tarefa: Task):
    tarefas = load_tasks()
    for idx, t in enumerate(tarefas):
        if t.id == id:
            tarefas[idx] = tarefa
            save_tasks(tarefas)
            return tarefa
    raise HTTPException(status_code=404, detail="Tarefa não encontrada.")

@app.delete("/tarefas/{id}", summary="Excluir tarefa")
def excluir_tarefa(id: int):
    tarefas = load_tasks()
    tarefas_novas = [t for t in tarefas if t.id != id]
    if len(tarefas_novas) == len(tarefas):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    save_tasks(tarefas_novas)
    return {"detail": "Tarefa excluída com sucesso."}

# -------------------------
# Execução (modo script)
# -------------------------

if __name__ == "__main__":
    import uvicorn
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", 3000))
    reload = os.getenv("API_RELOAD", "true").lower() == "true"
    uvicorn.run(app, host=host, port=port, reload=reload)
