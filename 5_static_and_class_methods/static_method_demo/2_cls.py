from typing import List


class Pizza:
    def __init__(self, ingredients: List[str] = []):
        self.ingredients = ingredients

    @classmethod
    def margherita(cls):
        return cls(["tomato sauce", "mozzarella", "fresh basil", "extra-virgin olive oil"])

    @classmethod
    def pepperoni(cls):
        return cls(["tomato sauce", "mozzarella", "pepperoni"])

    @classmethod
    def hawaiian(cls):
        return cls(["tomato sauce", "mozzarella", "ham", "pineapple"])

    @classmethod
    def quattro_for_maggi(cls):
        return cls(["tomato sauce", "mozzarella", "gorgonzola", "parmesan", "fontina"])


margherita = Pizza.margherita()
pepperoni = Pizza.pepperoni()
hawaiian = Pizza.hawaiian()
quattro_for_maggi = Pizza.quattro_for_maggi()

print(margherita.ingredients)
print(pepperoni.ingredients)
print(hawaiian.ingredients)
print(quattro_for_maggi.ingredients)
