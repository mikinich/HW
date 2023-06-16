import requests

def get_fastest_ship():
    response = requests.get("https://swapi.dev/api/starships/")
    ships_data = response.json()
    fastest = max(ships_data["results"], key=lambda ship: int(ship["max_atmosphering_speed"]))
    name = fastest["name"]
    speed = fastest["max_atmosphering_speed"]
    return speed
print(get_fastest_ship())