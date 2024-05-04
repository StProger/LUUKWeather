import aiohttp

from datetime import datetime


class MeteoData:

    @staticmethod
    async def get_meteo_data(lat, lon):

        url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"

        params = {
            "lat": lat,
            "lon": lon
        }

        async with aiohttp.ClientSession() as session:

            response = await session.get(url, params=params)
        if response.status == 200:

            data = (await response.json())["properties"]["timeseries"]
            weather_list = []
            left_dates = set()

            for index, weather_data in enumerate(data):

                date = datetime.fromisoformat(weather_data["time"])
                if date.day in left_dates:
                    continue
                # if date.day in left_dates:
                #     continue

                if date.hour == 14:
                    details = weather_data["data"]["instant"]["details"]
                    weather_list.append(
                        {
                            "air_temperature": details["air_temperature"],
                            "wind_speed": details["wind_speed"],
                            "date": date.strftime("%d %B, %A, %H:%M")
                        }
                    )
                    left_dates.add(date.day)
                elif date.hour > 14:

                    prev_date = date.fromisoformat(data[index-1]["time"])
                    if abs(14 - prev_date.hour) < abs(14 - date.hour):

                        details = data[index-1]["data"]["instant"]["details"]
                        weather_list.append(
                            {
                                "air_temperature": details["air_temperature"],
                                "wind_speed": details["wind_speed"],
                                "date": prev_date.strftime("%d %B, %A, %H:%M")
                            }
                        )
                        left_dates.add(prev_date.day)
                    else:
                        details = weather_data["data"]["instant"]["details"]
                        weather_list.append(
                            {
                                "air_temperature": details["air_temperature"],
                                "wind_speed": details["wind_speed"],
                                "date": date.strftime("%d %B, %A, %H:%M")
                            }
                        )
                        left_dates.add(date.day)


            return weather_list

        else:

            return None
