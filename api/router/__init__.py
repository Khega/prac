from fastapi import APIRouter
from api.src.endpoints import auth

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(auth.router, prefix="/goods", tags=["goods"])
