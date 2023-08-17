from sqlalchemy.orm import Session
import uuid
import models, schemas


def get_pessoa(db: Session, id: str):
    print(f"Procurou no banco o id {id}")
    return db.query(models.Pessoa).filter(models.Pessoa.id == id).first()

def get_pessoa_by_apelido(db: Session, apelido: uuid.UUID):
    return db.query(models.Pessoa).filter(models.Pessoa.apelido == apelido).first()

def search_pessoas(db: Session, t: str, skip: int = 0, limit: int = 50):
    print(f"TODO: Procurou no banco todas as pessoas com a query {t}")
    return db.query(models.Pessoa).limit(limit).all()
  
def count_pessoas(db: Session):
  return db.query(models.Pessoa).count()

def create_pessoa(db: Session, pessoa: schemas.PessoaBase):
    db_pessoa = models.Pessoa(apelido=pessoa.apelido, nome=pessoa.nome, nascimento=pessoa.nascimento, stack=pessoa.stack)
    db.add(db_pessoa)
    db.commit()
    db.refresh(db_pessoa)
    return db_pessoa