from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
import allure

class HomePage(BasePage):
    @allure.step('Нажать на кнопку куки')
    def click_button_cookies(self):
        button = self.find_element(HomePageLocators.COOKIES_BUTTON)
        button.click()

    @allure.step('Скролл до конца страницы')
    def scroll_page_to_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step('Выбрать вопрос из списка')
    def select_question(self, locator_question, locator_answer):
        question = self.find_element(locator_question)
        question.click()
        answer = self.find_element(locator_answer).text

        return answer

    @allure.step('Нажать на кнопку Заказать внизу')
    def click_order_button_center(self):
        button = self.find_element(HomePageLocators.ORDER_BUTTON_CENTER)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()

    @allure.step('Перейти на другую вкладку')
    def switch_to_other_tab(self):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])



























