from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)

    def listar_usuarios(self):
        return self.query(Usuario).all()
