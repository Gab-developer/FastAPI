from sqlalchemy.orm import sessionmaker
from models import db

def pegar_session():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
        # retorna valor sem encerrar a execução da função para conseguir fechar a sessão
    finally:
        session.close()