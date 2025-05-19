from geocoding_service import GeocodingService
from utils import get_user_input, display_coordinates, display_error

def main() -> None:
    place_name = get_user_input("Enter a place: ")
    geocoder = GeocodingService()
    result = geocoder.fetch_coordinates(place_name)

    if result.success:
        display_coordinates(result.latitude, result.longitude)
    else:
        display_error(result.error_message)

if __name__ == "__main__":
    main()
