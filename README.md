# qa_python
1. Тест test_add_new_book_add_two_books(self) - Добавление двух книг
2. Тест test_add_new_book_add_one_book_book_is_added(self) - Добавление одной книги
3. Тест test_add_new_book_re_add_book_book_not_added(self) - Добавление одной и той же книги повторно
4. тест test_set_book_rating_not_added_book_rating_not_added(self) - Нельзя добавить рейтинг книге, которой нет в списке
5. Тест test_set_books_rating_zero_rating_rating_not_added(self) - Нельзя добавить рейтинг книге меньше 1
6. Тест test_set_books_rating_eleven_rating_rating_not_added(self) - Нельзя добавить рейтинг книге выше 10
7. Тест test_get_book_rating_not_added_book_rating_not_added(self) - Отсутствие рейтинга у не добавленной книги
8. Тест test_get_books_with_specific_rating_list_five_rating_list_of_books_rated_five(self) - Вывод списка книг с определенным рейтингом
9. Тест test_get_books_rating_book_list_returns_a_list_of_books(self) - Вывод списка книг
10. Тест test_add_book_in_favorites_added_book_book_is_added(self) - Добавление книги в избранное
11. Тест test_add_book_in_favorites_not_added_book_book_not_added(self) - Нельзя добавить книгу в избранное, если её нет в словаре books_rating
12. Тест test_delete_book_from_favorites_book_added_to_favorites_the_book_is_deleted(self) - Удаление книги из избранного
13. Тест test_get_list_of_favorites_books_book_list_returns_a_list_of_favorite_books(self) - Вывод списка избранных книг