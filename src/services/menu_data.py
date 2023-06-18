from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.ingredients = set()
        self.source_path = source_path

    def read_file(self):
        with open(self.source_path, "r") as file:
            pass
