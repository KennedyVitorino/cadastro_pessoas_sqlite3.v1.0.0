from sqlalchemy import create_engine
from usuario import Base


def criar_banco_de_dados():
    engine = create_engine('sqlite:///cadastro_pessoas.db')
    Base.metadata.create_all(engine)
