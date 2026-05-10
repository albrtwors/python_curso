class Battle:

    @staticmethod
    def battle_turn(pokemon1, pokemon2):
        pokemon1.life-=pokemon2.attack
        pokemon2.life-=pokemon1.attack
        print(f"{pokemon1.name} tiene {pokemon1.life} puntos de vida| {pokemon2.name} tiene {pokemon2.life} puntos de vida")

