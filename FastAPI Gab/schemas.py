from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    nome: str
    data_nasc: str
    endereco: str
    sexo: str
    tem_carro: Optional[bool]

class UserResponse(UserSchema):
    id: int

    class Config:
        from_atributer = True