def get_user_input(prompt: str) -> str:
    return input(prompt).strip()

def display_coordinates(latitude: float, longitude: float) -> None:
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

def display_error(message: str) -> None:
    print(f"Error: {message}")