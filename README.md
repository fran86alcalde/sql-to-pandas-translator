# SQL to Pandas Translator 🐼

Small MVP that translates simple SQL queries into equivalent **pandas** code.

The goal of this project is not to fully replace SQL engines, but to help with:
- Learning pandas from SQL
- Quickly moving from SQL logic to Python analysis
- Prototyping and experimentation

This is a **demo / proof of concept**, not a production-ready translator.

---

## Features

- Translate basic SQL queries into pandas code
- Supported clauses (MVP):
  - SELECT
  - WHERE (simple conditions)
  - ORDER BY
  - LIMIT
- Web UI built with Streamlit
- REST API built with FastAPI
- Fully dockerized (one command to run everything)

---

## Architecture

- **Backend**: FastAPI  
  Exposes an API endpoint that receives SQL and returns pandas code.
- **Frontend**: Streamlit  
  Simple UI to paste SQL and visualize the translated pandas code.
- **Docker Compose**  
  Runs backend and frontend together.

---

## Run with Docker (recommended)

### Requirements
- Docker
- Docker Compose

### Start the app

```bash
docker compose up --build