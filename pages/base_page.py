import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_page_locators import BasePageLocators

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, delay=5):
        return WebDriverWait(self.driver, delay).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Перейти на сайт')
    def go_to_site(self, url):
        return self.driver.get(url)

    @allure.step('Получить текущий url')
    def get_current_url(self):
        current_url = self.driver.current_url

        return current_url

    @allure.step('Нажать на кнопку Заказать вверху')
    def click_order_button_top(self):
        button = self.find_element(BasePageLocators.ORDER_BUTTON_TOP)
        button.click()

    @allure.step('Нажать на лого Самокат')
    def click_scooter_button(self):
        button = self.find_element(BasePageLocators.BUTTON_SCOOTER)
        button.click()

    @allure.step('Нажать на лого Яндекс')
    def click_yandex_button(self):
        button = self.find_element(BasePageLocators.BUTTON_YANDEX)
        button.click()


