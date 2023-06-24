from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon_list: list[str] = []

    def add_pokemon(self, pokemon: Pokemon):
        if any([p.name == pokemon.name for p in self.pokemon_list]):  # True or False
            return "This pokemon is already caught"
        else:
            self.pokemon_list.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str, ):
        for pok in self.pokemon_list:
            if pok.name == pokemon_name:
                self.pokemon_list.remove(pok)
                return f"You have released {pokemon_name}"

        return f"Pokemon is not caught"


    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon_list)}"

        for p in self.pokemon_list:
            result += "\n" + f"- {p.pokemon_details()}"

        return result