from sqlalchemy import Boolean, Column, Integer, String, Date, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from database import Base
import uuid

class Pessoa(Base):
    __tablename__ = "pessoas"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    apelido = Column(String, unique=True, index=True, nullable=False)
    nome = Column(String, nullable=False)
    nascimento = Column(Date, nullable=False)
    stack = Column("stack", ARRAY(String))
