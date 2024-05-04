from fastapi import APIRouter
from starlette.requests import Request
from starlette.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="frontend/templates")


@router.get("/")
async def menu(request: Request):
    return templates.TemplateResponse(name="index.html", context={"request": request})
