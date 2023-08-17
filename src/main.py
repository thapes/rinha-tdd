from fastapi import Depends, FastAPI, HTTPException, Response
from sqlalchemy.orm import Session
import crud, models, schemas
import json

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/pessoas", response_model=schemas.Pessoa)
async def create_pessoa(pessoa: schemas.PessoaBase, response: Response, db: Session = Depends(get_db)):
    db_pessoa = crud.get_pessoa_by_apelido(db, apelido=pessoa.apelido)
    if db_pessoa:
        raise HTTPException(status_code=400, detail="Esse apelido já existe.")
    created = crud.create_pessoa(db=db, pessoa=pessoa)
    response.headers["Location"] = f"/pessoas/{created.id}"
    return created

@app.get("/pessoas/{pessoa_id}", response_model=schemas.Pessoa)
async def read_pessoa(pessoa_id: str, db: Session = Depends(get_db)):
    db_pessoa = crud.get_pessoa(db, id=pessoa_id)
    if db_pessoa is None:
        raise HTTPException(status_code=404, detail="Pessoa not found")
    return db_pessoa

@app.get("/pessoas", response_model=list[schemas.Pessoa])
async def search_pessoas(t: str, db: Session = Depends(get_db)):
    pessoas = crud.search_pessoas(db, t)
    return pessoas

@app.get("/contagem-pessoas/")
async def count_pessoas(db: Session = Depends(get_db)):
    return str(crud.count_pessoas(db))

