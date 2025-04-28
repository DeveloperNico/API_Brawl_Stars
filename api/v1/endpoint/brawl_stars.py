from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.brawl_stars_model import BrawlModel
from schemas.brawl_schemas import BrawlSchemas
from core.deps import get_session

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BrawlSchemas)
async def post_brawler(brawler: BrawlSchemas, db: AsyncSession = Depends(get_session)):
    novo_brawler = BrawlModel(nome=brawler.nome, ataque=brawler.ataque,
                                 ataque_super=brawler.ataque_super, saude=brawler.saude,
                                 raridade=brawler.raridade, foto=brawler.foto)
    db.add(novo_brawler)
    await db.commit()
    return novo_brawler

@router.get("/", response_model=List[BrawlSchemas])
async def get_brawlers(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(BrawlModel)
        result = await session.execute(query)
        brawlers: List[BrawlModel] = result.scalars().all()

        return brawlers
    
@router.get("/{brawler_id}", response_model=BrawlSchemas)
async def get_brawler(brawler_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(BrawlModel).filter(BrawlModel.id == brawler_id)
        result = await session.execute(query)
        brawler = result.scalar_one_or_none()

        if brawler:
            return brawler
        else:
            raise HTTPException(detail="Brawler não encontrado", status_code=status.HTTP_404_NOT_FOUND)
        
@router.put("/{brawler_id}", response_model=BrawlSchemas, status_code=status.HTTP_202_ACCEPTED)
async def put_brawler(brawler_id: int, brawler: BrawlSchemas, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(BrawlModel).filter(BrawlModel.id == brawler_id)
        result = await session.execute(query)
        brawler_up = result.scalar_one_or_none()

        if brawler_up:
            brawler_up.nome = brawler.nome
            brawler_up.ataque = brawler.ataque
            brawler_up.ataque_super = brawler.ataque_super
            brawler_up.saude = brawler.saude
            brawler_up.raridade = brawler.raridade
            brawler_up.foto = brawler.foto

            await session.commit()
            return brawler_up
        
        else:
            raise HTTPException(detail="Brawler não encontrado", status_code=status.HTTP_404_NOT_FOUND)
        
@router.delete("/{brawler_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_brawler(brawler_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(BrawlModel).filter(BrawlModel.id == brawler_id)
        result = await session.execute(query)
        brawler_del = result.scalar_one_or_none()

        if brawler_del:
            await session.delete(brawler_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Brawler não encontrado", status_code=status.HTTP_404_NOT_FOUND)
