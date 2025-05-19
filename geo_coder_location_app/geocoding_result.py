from typing import Optional

class GeocodingResult:
    def __init__(self, success: bool, latitude: Optional[float] = None, longitude: Optional[float] = None, error_message: Optional[str] = None):
        self.success = success
        self.latitude = latitude
        self.longitude = longitude
        self.error_message = error_message

    @staticmethod
    def success_result(lat: float, lon: float) -> "GeocodingResult":
        return GeocodingResult(success=True, latitude=lat, longitude=lon)

    @staticmethod
    def failure_result(message: str) -> "GeocodingResult":
        return GeocodingResult(success=False, error_message=message)
