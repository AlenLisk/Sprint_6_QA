from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
import allure

class HomePage(BasePage):
    @allure.step('Нажать на кнопку куки')
    def click_button_cookies(self):
        button = self.find_element(HomePageLocators.COOKIES_BUTTON)
        button.click()

    @allure.step('Выбрать вопрос из списка')
    def select_question(self, number_question):
        home_page_locators = HomePageLocators()
        locator_question, locator_answer = home_page_locators.question_locator_generator(number_question)

        question = self.find_element(locator_question)
        question.click()
        answer = self.find_element(locator_answer).text

        return answer

    @allure.step('Нажать на кнопку Заказать внизу')
    def click_order_button_center(self):
        button = self.find_element(HomePageLocators.ORDER_BUTTON_CENTER)
        self.scroll_to_element(button)
        button.click()



























