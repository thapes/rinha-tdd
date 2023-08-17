from pydantic import BaseModel
from datetime import date
from typing import Optional
import uuid



class PessoaBase(BaseModel):
  apelido: str
  nome: str
  nascimento: date
  stack: Optional[list[str]] = None

class Pessoa(PessoaBase):
  id: uuid.UUID
