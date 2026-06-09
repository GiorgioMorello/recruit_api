from sqlalchemy import Column, Integer, String
from database import Base
import uuid

class Client(Base):
    __tablename__ = "clients"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    tel = Column(String, unique=True, nullable=True)
    score = Column(Integer, default=0)
    birth_date = Column(String, nullable=True)
    cpf = Column(String, nullable=True)
    instagram_facebook = Column(String, nullable=True)
    professional_situation = Column(String, nullable=True)
    cep = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)