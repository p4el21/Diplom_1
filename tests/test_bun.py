import allure
from ya_praktikum.bun import Bun

class TestBun:
    @allure.title('Проверка инициализации булочки')
    @allure.description('Тест проверяет, что булочка инициализируется с правильными данными')
    def test_init_bun(self):
        bun = Bun('Булочка', 100)
        assert bun.get_name() == 'Булочка', f"Ожидается название булочки: Булочка"
        assert bun.get_price() == 100, f"Ожидается цена булочки: 100"
        print('\nТест пройден!')

    @allure.title('Проверка инициализации булочки с неправильными данными')
    @allure.description('Тест проверяет, что булочка инициализируется с неправильными данными')
    def test_init_bun_with_wrong_data(self):
        bun = Bun(100, 'Булочка')
        assert bun.get_name() == 100, f"Ожидается название булочки: 100"
        assert bun.get_price() == 'Булочка', f"Ожидается цена булочки: Булочка"
        print('\nТест пройден!')

    @allure.title('Проверка изменении названии булочки')
    @allure.description('Тест проверяет, что можно изменить название булочки')
    def test_name_change(self):
        bun = Bun('Булочка', 100)
        bun.name = 'Булка'
        assert bun.get_name() == 'Булка', f"Ожидается название булочки: Булка"
        print('\nТест пройден!')

    @allure.title('Проверка изменении цены булочки')
    @allure.description('Тест проверяет, что можно изменить цену булочки')
    def test_price_change(self): #Изменение цены булочки
        bun = Bun('Булочка', 100)
        bun.price = 500
        assert bun.get_price() == 500, f"Ожидается цена булочки: 5"
        print('\nТест пройден!')



