import requests
from config import OPENWEATHER_API_KEY, GEOCODING_URL
from geocoding_result import GeocodingResult

class GeocodingService:
    def __init__(self, api_key: str = OPENWEATHER_API_KEY):
        self.api_key = api_key

    def fetch_coordinates(self, place_name: str) -> GeocodingResult:
        if not self.api_key:
            return GeocodingResult.failure_result("API key is missing.")

        params = {
            "q": place_name,
            "limit": 1,
            "appid": self.api_key
        }

        try:
            response = requests.get(GEOCODING_URL, params=params)
            response.raise_for_status()
        except requests.RequestException as e:
            return GeocodingResult.failure_result(f"Network error: {e}")

        data = response.json()
        if not data:
            return GeocodingResult.failure_result(f"No results found for '{place_name}'.")

        location = data[0]
        return GeocodingResult.success_result(location["lat"], location["lon"])
