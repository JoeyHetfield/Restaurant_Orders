from src.models.dish import Dish  # noqa: F401, E261, E501


# Req 2
def test_dish():
    food = Dish("hamburguer", 15.0)
    assert food.name == "hamburguer"

    food2 = Dish("pizza", 27.0)
    assert food2.name != food.name
    assert food2 != food

    food3 = Dish("hamburguer", 15.0)
    assert food3.name == food.name
    assert food3 == food
