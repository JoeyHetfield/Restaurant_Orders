from src.models.dish import Dish
from src.models.ingredient import Ingredient
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.ingredients = set()
        self.source_path = source_path
        self.read_file()

    def read_file(self):
        with open(self.source_path, "r") as file:
            reader = csv.reader(file)
            next(reader)

            dishes = {}

            for row in reader:
                dish_name = row[0]
                dish_price = float(row[1])
                ingredient_name = row[2]
                ingredient_quantity = int(row[3])

                if dish_name not in dishes:
                    dish = Dish(dish_name, dish_price)
                    dishes[dish_name] = dish
                    self.dishes.add(dish)
                else:
                    dish = dishes[dish_name]

                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, ingredient_quantity)
                self.ingredients.add(ingredient)
