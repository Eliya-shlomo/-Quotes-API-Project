import requests

import requests

import requests
from urllib.parse import quote

def get_all_quotes(philosopher):
    BASE_URL = "http://127.0.0.1:5000"

    encoded_philosopher = quote(philosopher)
    response = requests.get(f"{BASE_URL}/quotes/philosopher/{encoded_philosopher}")

    try:
        if response.status_code == 200:
            print(f"Quotes by {philosopher}:", response.json())
        else:
            print(f"Error fetching quotes for {philosopher}:", response.json())
    except requests.exceptions.JSONDecodeError:
        print(f"Error: Server returned a non-JSON response. Status code: {response.status_code}")



def add_new_quote(philosopher, new_quote):
    BASE_URL = "http://127.0.0.1:5000"

    encoded_philosopher = quote(philosopher)

    if "quote" not in new_quote or not new_quote["quote"].strip():
        print("error: A valid citation must be provided.")
        return

    response = requests.post(f"{BASE_URL}/quotes/philosopher/{encoded_philosopher}", json=new_quote)

    try:
        if response.status_code == 201:
            print("citaion upload successfully", response.json())
        else:
            print("error on upload the citaion:", response.json())
    except requests.exceptions.JSONDecodeError:
        print(f"error The server returned an invalid response.: {response.status_code}")


def get_characters_with_hight_over(trashhold):
    url = "https://swapi.dev/api/people/"

    characters = []

    while url: 
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            for character in data['results']:
                try:
                    height = int (character['height']);
                    if height < trashhold:
                        characters.append({
                            'name': character['name'],
                            'height': height
                        })

                except ValueError:
                    continue

            url = data['next'];
        else:
            print(f'Failed to fetch data {response.status_code}')
            break;
    return characters

# print(f'get all characters with height over 172')
# filtered_characters = get_characters_with_hight_over(172);
# for char in filtered_characters:
#     print(f'Name:{char['name']} Height:{char['height']}')


import requests

def get_all_spaceship_with_capacity_over(threshold):
    url = 'https://swapi.dev/api/starships/'
    starships = []  # Keep this as a list to collect filtered starships

    while url:  # Handle pagination
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()

            for ship in data['results']:  # Use a different variable name (e.g., `ship`)
                try:
                    capacity = int(ship['crew'].replace(',', ''))  # Handle comma-separated numbers

                    if capacity > threshold:
                        starships.append({
                            'name': ship['name'],
                            'capacity': capacity
                        })
                except (ValueError, KeyError):  # Handle invalid or missing data
                    continue

            url = data['next']  # Get the next page URL
        else:
            print(f"Error fetching data: {response.status_code}")
            break

    return starships

# Call the function and filter ships with crew capacity > 7000
filtered_starships = get_all_spaceship_with_capacity_over(7000)

# Print the results
# for starship in filtered_starships:
#     print(f"Name: {starship['name']}, Capacity: {starship['capacity']}")


def all_creatures_their_name_contain_char(trashhold):
     
    url = 'https://swapi.dev/api/species/'

    response = requests.get(url)

    creatures = []

    if response.status_code == 200:
        data = response.json()

        for creature in data['results']:
            try:
                    
                name = creature['name'];

                if trashhold in name:
                    creatures.append({
                        'name': name
                    })
            except(ValueError,KeyError):
                continue
        url = data['next']
    else:
        print(f'error on fetching data{response.status_code}')
        url = None
    return creatures


filtered_creatures = all_creatures_their_name_contain_char('W')

# for creature in filtered_creatures:
#     print(f'name:{creature['name']}')


def filter_by_maxium_speed(trashhold):

    url = "https://swapi.dev/api/starships/"

    response = requests.get(url)

    starships = []

    if response.status_code == 200:

        data = response.json()

        for ship in data['results']:

            try:

                max_speed = int(ship['max_atmosphering_speed'].replace(',',''))

                if max_speed > trashhold:
                    starships.append({
                        'name': ship['name'],
                        'max_speed': max_speed,
                        'cargo_capacity' :ship['cargo_capacity']
                    })
            except (ValueError,KeyError):
                continue
        url = data['next']
    else:
        print(f'error on fetching data{response.status_code}')
        url = None

    sorted_starship = sorted(
        starships,
        key = lambda x:int(x['cargo_capacity']) if x['cargo_capacity'].isdigit() else 0,
        reverse=True
    )
    return sorted_starship


# filtered_ships = filter_by_maxium_speed(1000) 
# for ship in filtered_ships:
#     print(f'name: {ship['name']}, max_speed: {ship['max_speed']}, cargo_capacity: {ship['cargo_capacity']}')


get_all_quotes("ניטשה")



    

                

        

