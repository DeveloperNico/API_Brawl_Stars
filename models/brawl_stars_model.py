from core.configs import settings
from sqlalchemy import Column, Integer, String

class BrawlModel(settings.DBBaseModel):
    __tablename__ = "personagem"

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: str = Column(String(256))
    ataque: str = Column(String(256))
    ataque_super: str = Column(String(256))
    saude: int = Column(Integer())
    raridade: str = Column(String(256))
    foto: str = Column(String(256))