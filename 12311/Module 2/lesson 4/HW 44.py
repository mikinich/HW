import requests

response = requests.get('https://swapi.dev/api')
starships_api = response.json()['starships']
Ships_list = []
Speed =[]
response = requests.get(starships_api)

for i in range(2,7):
    SSU = f'{starships_api}{i}'
    response = requests.get(SSU)
    # print(SSU)
    # print(response.json())
    data = response.json()
    Ships_list.append(data['max_atmosphering_speed'])
    Speed.append(data['max_atmosphering_speed'])
    # Speed.sort(reverse=1)

print(Speed)

# Выведите максимальную скорость 5 космических кораблей.
#
# API — starships_api = response.get('starships')
#
# Максимальная скорость — max_atmosphering_speed