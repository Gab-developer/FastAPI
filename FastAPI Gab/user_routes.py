from fastapi import APIRouter, Depends, HTTPException
from models import Users
from dependencies import pegar_session
from schemas import UserSchema
from sqlalchemy.orm import Session

user_router = APIRouter(prefix="/users", tags=["Usuários"])

@user_router.get("/")
async def listar_users(session: Session = Depends(pegar_session)):
    users = session.query(Users).all()
    return users


@user_router.post("/create_user")
async def criar_usuario(UserSchema: UserSchema, session: Session = Depends(pegar_session)):
    novo_user = Users(UserSchema.nome, UserSchema.data_nasc, UserSchema.endereco, UserSchema.sexo, UserSchema.tem_carro)
    session.add(novo_user)
    session.commit()
    return {"message": "Usuário cadastrado com sucesso!"}



@user_router.put("/update_user/{user_id}")
async def atualizar_usuario(
    user_id: int,
    dados: UserSchema,
    session: Session = Depends(pegar_session)
):
    
    user = session.query(Users).filter(Users.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    user.nome = dados.nome
    user.data_nasc = dados.data_nasc
    user.endereco = dados.endereco
    user.sexo = dados.sexo
    user.tem_carro = dados.tem_carro

    session.commit()
    
    return {"message": "Usuário atualizado com sucesso!"}



@user_router.delete("/delete_user/{user_id}")
async def deletar_usuario(
    user_id: int,
    session: Session = Depends(pegar_session)
):
    
    user = session.query(Users).filter(Users.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    session.delete(user)
    session.commit()

    return {"message": "Usuário deletado com sucesso!"}