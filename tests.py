from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Добавление книги
    def test_add_new_book_add_one_book_book_is_added(self):
        collector = BooksCollector()

        collector.add_new_book('Маленький принц')

        assert len(collector.get_books_rating()) == 1

    # Добавление одной и той же книги повторно
    def test_add_new_book_re_add_book_book_not_added(self):
        collector = BooksCollector()

        collector.add_new_book('Искусство любить')
        collector.add_new_book('Искусство любить')

        assert len(collector.get_books_rating()) == 1

    # Нельзя добавить рейтинг книге, которой нет в списке
    def test_set_book_rating_not_added_book_rating_not_added(self):
        collector = BooksCollector()

        collector.set_book_rating('Пять языков любви', 5)

        assert len(collector.get_books_rating()) == 0

    # Нельзя добавить рейтинг книге меньше 1
    def test_set_books_rating_zero_rating_rating_not_added(self):
        collector = BooksCollector()

        collector.add_new_book('Два капитана')
        collector.set_book_rating('Два капитана', 0)

        assert collector.get_book_rating('Два капитана') == 1

    # Нельзя добавить рейтинг книге выше 10
    def test_set_books_rating_eleven_rating_rating_not_added(self):
        collector = BooksCollector()

        collector.add_new_book('Капитанская дочка')
        collector.set_book_rating('Капитанская дочка', 11)

        assert collector.get_book_rating('Капитанская дочка') == 1

    # Отсутствие рейтинга у не добавленной книги
    def test_get_book_rating_not_added_book_rating_not_added(self):
        collector = BooksCollector()

        assert collector.get_book_rating('Принцесса на горошине') == None

    # Вывод списка книг с определенным рейтингом
    def test_get_books_with_specific_rating_list_five_rating_list_of_books_rated_five(self):
        collector = BooksCollector()

        collector.add_new_book('Человек, который принял жену за шляпу')
        collector.add_new_book('Горе от ума')
        collector.set_book_rating('Горе от ума', 5)

        assert collector.get_books_with_specific_rating(5)[0] == 'Горе от ума' and len(collector.get_books_with_specific_rating(5)) == 1

    # Вывод списка книг
    def test_get_books_rating_book_list_returns_a_list_of_books(self):
        collector = BooksCollector()

        collector.add_new_book('Властелин овец')
        collector.add_new_book('Хоббит туда-сюда')

        assert len(collector.get_books_rating()) == 2

    # Добавление книги в избранное
    def test_add_book_in_favorites_added_book_book_is_added(self):
        collector = BooksCollector()

        collector.add_new_book('Продавец воздуха')
        collector.add_new_book('Власть тьмы')
        collector.add_book_in_favorites('Продавец воздуха')

        assert collector.get_list_of_favorites_books()[0] == 'Продавец воздуха' and len(collector.get_list_of_favorites_books()) == 1

    # Нельзя добавить книгу в избранное, если её нет в словаре books_rating
    def test_add_book_in_favorites_not_added_book_book_not_added(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Как управлять рабами')

        assert len(collector.get_list_of_favorites_books()) == 0

    # Удаление книги из избранного
    def test_delete_book_from_favorites_book_added_to_favorites_the_book_is_deleted(self):
        collector = BooksCollector()

        collector.add_new_book('Мой дедушка был вишней')
        collector.add_book_in_favorites('Мой дедушка был вишней')
        collector.get_list_of_favorites_books() == 1
        collector.delete_book_from_favorites('Мой дедушка был вишней')

        assert  len(collector.get_list_of_favorites_books()) == 0

    # Вывод списка избранных книг
    def test_get_list_of_favorites_books_book_list_returns_a_list_of_favorite_books(self):
        collector = BooksCollector()

        collector.add_new_book('Сочные глазки и пижама в лягушечку')
        collector.add_book_in_favorites('Сочные глазки и пижама в лягушечку')

        assert len(collector.get_list_of_favorites_books()) == 1