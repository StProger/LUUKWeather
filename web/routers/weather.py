from fastapi import APIRouter

from web.exceptions import IncorrectInputException

from web.service.weather.meteo import MeteoData

from starlette.requests import Request
from starlette.templating import Jinja2Templates


router = APIRouter(
    prefix="/weather",
    tags=["Погода"]
)

templates = Jinja2Templates(directory="frontend/templates")


@router.get("")
async def weather(request: Request,
                  lat: float = 55.7522,
                  lon: float = 37.6156):
    """
    :param request: Request
    :param lat: Широта в десятичных градусах
    :param lon: Долгота в десятичных градусах
    :return:
    """
    data = await MeteoData.get_meteo_data(lat=lat, lon=lon)

    if data:
        return templates.TemplateResponse(name="weather.html", context={"request": request, "weather_data": data})
    else:

        raise IncorrectInputException()
