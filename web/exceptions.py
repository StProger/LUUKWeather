from fastapi import status, HTTPException


class WeatherException(HTTPException):

    status_code = 500
    detail = ""

    def __init__(self):

        super().__init__(status_code=self.status_code, detail=self.detail)


class IncorrectInputException(WeatherException):

    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Incorrect input data"
