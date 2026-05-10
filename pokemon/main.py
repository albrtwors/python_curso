
from src.battle import Battle
from pokemons.charmander import Charmander          
from pokemons.squirtle import Squirtle
from src.helloWorld import hello_mum, hello_world
from src.suma import suma

pokemon_1=Charmander({'name':'Lagarto', 'life':30, 'attack':4})
pokemon_2=Squirtle({'name':'Tortuga', 'life':30, 'attack':5})

while pokemon_1.life > 0 and pokemon_2.life>0:
    print('Turno de batalla')
    Battle.battle_turn(pokemon_1, pokemon_2)
    if pokemon_1.life<=0:
        print(f'Gana {pokemon_2.name}')
    else:
        print(f'Gana {pokemon_1.name}')    


# #python3 -m main

# sum1 = suma(10, 5)

# print(f"Suma de ambos números: {sum1.calculo()}")