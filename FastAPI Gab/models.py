from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.orm import declarative_base

db = create_engine("sqlite:///banco.db")
 
Base = declarative_base()

class Users(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    data_nasc = Column("data_nascimento", String)
    endereco = Column("endereco", String)
    sexo = Column("sexo", String)
    tem_carro = Column("tem_carro", Boolean, default=False)

    def __init__(self, nome, data_nasc, endereco, sexo, tem_carro=False):
        self.nome = nome
        self.data_nasc = data_nasc
        self.endereco = endereco
        self.sexo = sexo
        self.tem_carro = tem_carro
