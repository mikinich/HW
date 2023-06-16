import requests
def MAX_D():

    response = requests.get('https://swapi.dev/api')
    planets_url = response.json()['planets']
    planets_list = []
    diameter =[]
    response = requests.get(planets_url)

    for i in range(1,6):
        DPU = f'{planets_url}{i}'
        response = requests.get(DPU)
        data = response.json()
        data['diameter'] = int(data['diameter'])
        # print(response.json())
        planets_list.append(data)
        diameter.append(data['diameter'])
        diameter.sort(reverse=1)
    return diameter[0]