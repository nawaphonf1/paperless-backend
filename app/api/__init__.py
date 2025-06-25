from fastapi import APIRouter
from app.api.routes import units, dropdown, permission,categories, doc, dashboad

api_router = APIRouter()

api_router.include_router(units.router, prefix="/unit", tags=["unit"])
api_router.include_router(dropdown.router, prefix="/dropdown", tags=["dropdown"])
api_router.include_router(permission.router, prefix="/permission", tags=["permission"])
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(doc.router, prefix="/doc", tags=["doc"])
api_router.include_router(dashboad.router, prefix="/dashboard", tags=["dashboard"])





