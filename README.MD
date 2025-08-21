# FastAPI Starter

Este projeto é uma API simples utilizando [FastAPI](https://fastapi.tiangolo.com/) com suporte a CORS e configuração flexível via variáveis de ambiente.

## Funcionalidades

- **FastAPI**: Framework moderno e rápido para APIs em Python.
- **CORS Middleware**: Permite requisições de qualquer origem.
- **Endpoint inicial**: Verifica se a API está online.
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
uvicorn app:app --host 0.0.0.0 --port 7090 --reload
```

A API estará disponível em [http://localhost:7090](http://localhost:7090).

## Variáveis de Ambiente

- `API_HOST`: Host da aplicação (padrão: `0.0.0.0`)
- `API_PORT`: Porta da aplicação (padrão: `7090`)
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
    "description": "Bem vindo a API"
  }
  ```

---

> Projeto básico para iniciar aplicações