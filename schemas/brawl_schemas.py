from typing import Optional
from pydantic import BaseModel as SCBaseModel

class BrawlSchemas(SCBaseModel):
    id: Optional[int] = None
    nome: str
    ataque: str
    ataque_super: str
    saude: int
    raridade: str
    foto: str

    class Config:
        from_atributes = True