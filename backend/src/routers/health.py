from fastapi import APIRouter
from src.database.database import client

health_router = APIRouter(tags=["Health"])


@health_router.get("/health")
def health():
    if client:
        data = {
            "overalSuccess": True
        }
        return data
    else:
        data = {
            "overalSuccess": False
        }
        return data