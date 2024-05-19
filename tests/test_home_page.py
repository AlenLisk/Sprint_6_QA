from conftest import *
from data import AnswerOptions
import allure
from urls import Urls


class TestHomePage:

    @pytest.mark.parametrize(
        "number_question, expected_answer",
        [
            (0, AnswerOptions.answer_1),
            (1, AnswerOptions.answer_2),
            (2, AnswerOptions.answer_3),
            (3, AnswerOptions.answer_4),
            (4, AnswerOptions.answer_5),
            (5, AnswerOptions.answer_6),
            (6, AnswerOptions.answer_7),
            (7, AnswerOptions.answer_8)
        ]
    )

    @allure.title('Проверка соответствия вопросов и ответов на главной странице')
    @allure.description('При нажатии на определенный вопрос на шлавной странице открывается соответствующий ответ')
    def test_select_questions(self, home_page, number_question, expected_answer):
        home_page.scroll_page_to_end()
        actual_answer = home_page.select_question(number_question)

        assert actual_answer == expected_answer

    @allure.title('Проверка перехода по лого Яндекс')
    @allure.description('При нажатии на лого Яндекс происходит переход на страницу Дзена')
    def test_click_button_yandex(self, home_page):
        expected_url = Urls.URL_DZEN
        home_page.click_yandex_button()
        home_page.switch_to_other_tab()
        actual_url = home_page.get_current_url()

        assert actual_url == expected_url

    @allure.title('Проверка нажатия на кнопку Заказать внизу')
    @allure.description('При нажатии на кнопку Заказать внизу страницы происходит переход на форму заказа')
    def test_click_order_button_center(self, home_page):
        expected_url = Urls.URL_ORDER

        home_page.click_order_button_center()
        actual_url = home_page.get_current_url()

        assert actual_url == expected_url

    @allure.title('Проверка нажатия на кнопку Заказать вверху')
    @allure.description('При нажатии на кнопку Заказать вверху страницы происходит переход на форму заказа')
    def test_click_order_button_top(self, home_page):
        expected_url = Urls.URL_ORDER

        home_page.click_order_button_top()
        actual_url = home_page.get_current_url()

        assert actual_url == expected_url
