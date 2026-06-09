from pydantic import BaseModel, ConfigDict
from typing import Optional



class ClientCreate(BaseModel):
    name: Optional[str] = None
    tel: Optional[str] = None
    score: Optional[int] = 0
    birth_date: Optional[str] = None
    cpf: Optional[str] = None
    instagram_facebook: Optional[str] = None
    professional_situation: Optional[str] = None
    cep: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    


class ClientResponse(ClientCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)
