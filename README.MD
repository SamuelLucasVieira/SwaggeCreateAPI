# FastAPI Starter

Este projeto é uma API simples utilizando [FastAPI](https://fastapi.tiangolo.com/) com suporte a CORS, CRUD de tarefas e persistência em arquivo JSON.

## Funcionalidades

- **FastAPI**: Framework moderno e rápido para APIs em Python.
- **CRUD de Tarefas**: Crie, liste, atualize e exclua tarefas.
- **Campos da Tarefa**: Cada tarefa possui `id`, `titulo`, `descricao` e `status` (pendente/concluída).
- **Persistência em JSON**: As tarefas são salvas em um arquivo `tasks.json`.
- **Validação de Status**: O campo `status` só aceita os valores "pendente" ou "concluída".
- **CORS Middleware**: Permite requisições de qualquer origem.
- **Configuração por variáveis de ambiente**: Host, porta e modo de recarregamento automático.

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/SamuelLucasVieira/SwaggeCreateAPI
   cd FastAPI
   ```

2. Crie um ambiente virtual e ative:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Como executar

Execute o comando abaixo na pasta `src`:

```sh
uvicorn app:app --host 0.0.0.0 --port 3000 --reload
```

A API estará disponível em [http://localhost:3000](http://localhost:3000).

## Variáveis de Ambiente

- `API_HOST`: Host da aplicação (padrão: `0.0.0.0`)
- `API_PORT`: Porta da aplicação (padrão: `3000`)
- `API_RELOAD`: Ativa recarregamento automático (padrão: `true`)

Exemplo de execução customizada:

```sh
set API_PORT=8000
set API_RELOAD=false
python app.py
```

## Endpoints

- `GET /`  
  **Descrição:** Verifica se a API está online.  
  **Resposta:**  
  ```json
  {
    "message": "API de Tarefas Online"
  }
  ```

- `GET /tarefas`  
  **Descrição:** Lista todas as tarefas cadastradas.  
  **Resposta:**  
  ```json
  [
    {
      "id": 1,
      "titulo": "Estudar FastAPI",
      "descricao": "Ler a documentação oficial",
      "status": "pendente"
    }
  ]
  ```

- `POST /tarefas`  
  **Descrição:** Cria uma nova tarefa.  
  **Payload:**  
  ```json
  {
    "id": 2,
    "titulo": "Fazer exercícios",
    "descricao": "Exercícios de FastAPI",
    "status": "pendente"
  }
  ```

- `PUT /tarefas/{id}`  
  **Descrição:** Atualiza uma tarefa existente pelo ID.  
  **Payload:**  
  ```json
  {
    "id": 2,
    "titulo": "Fazer exercícios",
    "descricao": "Exercícios de FastAPI",
    "status": "concluída"
  }
  ```

- `DELETE /tarefas/{id}`  
  **Descrição:** Exclui uma tarefa pelo ID.  
  **Resposta:**  
  ```json
  {
    "detail": "Tarefa excluída com sucesso."
  }
  ```

---

> Projeto básico para treinar rotas REST e persistência simples com FastAPI.