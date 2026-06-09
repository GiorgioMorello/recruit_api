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



class DataForEmail(BaseModel):
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
    product_exp: Optional[str] = None
    current_product: Optional[str] = None
    income: Optional[str] = None
    available_time: Optional[str] = None
    commercial_representative: Optional[str] = None
    motivation: Optional[str] = None 