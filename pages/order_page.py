import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Ввод имени')
    def set_name(self, name):
        field_name = self.find_element(OrderPageLocators.FIELD_NAME)
        field_name.send_keys(name)

    @allure.step('Ввод фамилии')
    def set_surname(self, surname):
        field_surname = self.find_element(OrderPageLocators.FIELD_SURNAME)
        field_surname.send_keys(surname)

    @allure.step('Ввод адреса')
    def set_address(self, address):
        field_address = self.find_element(OrderPageLocators.FIELD_ADDRESS)
        field_address.send_keys(address)

    @allure.step('Ввод метро')
    def set_metro(self, metro):
       order_page_locators = OrderPageLocators()
       METRO = order_page_locators.locators_generation(metro)[0]

       field_metro = self.find_element(OrderPageLocators.FIELD_METRO)
       field_metro.click()
       metro = self.find_element(METRO)
       metro.click()

    @allure.step('Ввод номера')
    def set_number(self, number):
        field_number = self.find_element(OrderPageLocators.FIELD_NUMBER)
        field_number.send_keys(number)

    @allure.step('Нажать на кнопку Далее')
    def click_button_farther(self):
        button = self.find_element(OrderPageLocators.BUTTON_FARTHER)
        button.click()

    @allure.step('Выбор даты')
    def set_date(self, date):
        field_date = self.find_element(OrderPageLocators.FIELD_DATE)
        field_date.send_keys(date)

    @allure.step('Выбор аренды')
    def set_rent(self, rent):
       order_page_locators = OrderPageLocators()
       RENT = order_page_locators.locators_generation(rent)[0]

       field_rent = self.find_element(OrderPageLocators.FIELD_RENT)
       field_rent.click()
       rent = self.find_element(RENT)
       rent.click()

    @allure.step('Выбор цвета')
    def set_color(self, color):
       order_page_locators = OrderPageLocators()
       COLOR = order_page_locators.locators_generation(color)[1]
       field_color = self.find_element(COLOR)
       field_color.click()

    @allure.step('Ввод комментария')
    def set_comment(self, comment):
       field_comment = self.find_element(OrderPageLocators.FIELD_COMMENT)
       field_comment.send_keys(comment)

    @allure.step('Нажать кнопку Заказать')
    def click_button_order(self):
        button = self.find_element(OrderPageLocators.BUTTON_ORDER)
        button.click()

    @allure.step('Нажать кнопку Да')
    def click_button_yes(self):
        button = self.find_element(OrderPageLocators.BUTTON_YES)
        button.click()

    @allure.step('Заполнить форму Для кого самокат')
    def fill_form_personal_info(self, data):
        self.set_name(data['name'])
        self.set_surname(data['surname'])
        self.set_address(data['address'])
        self.set_metro(data['metro'])
        self.set_number(data['number'])
        self.click_button_farther()

    @allure.step('Заполнить форму Куда привезти')
    def fill_form_rent_info(self, data):
        self.set_date(data['date'])
        self.set_rent(data['rent'])
        self.set_color(data['color'])
        self.set_comment(data['comment'])
        self.click_button_order()
        self.click_button_yes()


