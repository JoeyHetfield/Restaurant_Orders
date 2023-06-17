from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


def test_ingredient():
    item = Ingredient("bacon")
    assert item.name == "bacon"

    expected_repr = "Ingredient('bacon')"
    assert repr(item) == expected_repr

    item2 = Ingredient("frango")
    assert item2.name == "frango"

    assert item != item2
