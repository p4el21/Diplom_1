import allure
import pytest
from ya_praktikum.ingredient import Ingredient

class TestIngredient:
    @allure.title('Проверка инициализации ингридиента')
    @allure.description('Тест проверяет, что ингридиент инициализируется с правильными данными')
    @pytest.mark.parametrize('ingredient_type, name, price', [
        ('Соус', 'Сырный', 100),
        ('Начинка', 'Повидло', 200),
    ])
    def test_init_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type, f"Ожидается тип ингридиента: {ingredient_type}"
        assert ingredient.get_name() == name, f"Ожидается название ингридиента: {name}"
        assert ingredient.get_price() == price, f"Ожидается цена ингридиента: {price}"
        print('\nТест пройден!')

    @allure.title('Проверка получения типа ингридиента')
    @allure.description('Тест проверяет, что можно получить тип ингридиента')
    def test_type_change(self):
        ingredient = Ingredient('Соус', 'Сырный', 100)
        assert ingredient.get_type() == 'Соус', f"Ожидается тип ингридиента: Соус"
        print('\nТест пройден!')

    @allure.title('Проверка получения названия ингридиента')
    @allure.description('Тест проверяет, что можно получить название ингридиента')
    def test_name_change(self):
        ingredient = Ingredient('Соус', 'Сырный', 100)
        assert ingredient.get_name() == 'Сырный', f"Ожидается название ингридиента: Горчичный"
        print('\nТест пройден!')

    @allure.title('Проверка получения цены ингридиента')
    @allure.description('Тест проверяет, что можно получить цену ингридиента')
    def test_price_change(self):
        ingredient = Ingredient('Соус', 'Сырный', 100)
        assert ingredient.get_price() == 100, f"Ожидается цена ингридиента: 100"
        print('\nТест пройден!')


