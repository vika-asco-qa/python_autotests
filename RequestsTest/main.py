import requests

HOST = 'https://pokemonbattle.me:9104'
TOKEN = '5cd242c94a63f9c17384ba51c3dfa3fe'

#создание покемона
create_pokemon = requests.post(f'{HOST}/pokemons', headers = {'trainer_token': TOKEN}, json = {
    "name": "Курама",
    "photo": "https://www.pngmart.com/files/5/Kurama-PNG-Picture.png"
}).json()

print(create_pokemon)

#смена имени покемона
change_pokemon_name = requests.put(f'{HOST}/pokemons', headers = {'trainer_token': TOKEN}, json = {
    "pokemon_id": create_pokemon['id'],
    "name": "Сонгоку",
    "photo": "https://www.pngmart.com/files/5/Kurama-PNG-Picture.png"
}).json()

print(change_pokemon_name)

#добавления покемона в покебол
add_to_pokeball = requests.post(f'{HOST}/trainers/add_pokeball', headers = {'trainer_token': TOKEN}, json = {
    "pokemon_id": create_pokemon['id']
}).json()

print(add_to_pokeball)