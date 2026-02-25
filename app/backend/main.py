from fastapi import FastAPI
from pydantic import BaseModel
from app.backend.translator import sql_to_pandas

app = FastAPI(title="SQL to Pandas Translator")

class SQLRequest(BaseModel):
    query: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/translate")
def translate_sql(req: SQLRequest):
    pandas_code = sql_to_pandas(req.query)
    return {"pandas_code": pandas_code}
