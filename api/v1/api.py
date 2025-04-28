from fastapi import APIRouter

from api.v1.endpoint import brawl_stars

api_router = APIRouter()

api_router.include_router(brawl_stars.router, prefix="/brawler", tags=["Brawlers"])