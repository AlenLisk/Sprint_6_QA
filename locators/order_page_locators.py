from selenium.webdriver.common.by import By


class OrderPageLocators:

    FIELD_NAME = (By.XPATH, ".//input[@placeholder='* Имя']")
    FIELD_SURNAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    FIELD_ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    FIELD_METRO = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    FIELD_NUMBER = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_FARTHER = (By.XPATH, ".//button[text()='Далее']")
    FIELD_DATE = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    FIELD_RENT = (By.CLASS_NAME, 'Dropdown-arrow')
    FIELD_COMMENT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    BUTTON_ORDER = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    BUTTON_YES = (By.XPATH, ".//button[text()='Да']")
    MODAL_ORDER_HEADER = (By.XPATH, ".//div[@class = 'Order_ModalHeader__3FDaJ']")

    @staticmethod
    def locators_generation(data):
        METRO_RENT = (By.XPATH, f".//div[text()='{data}']")
        COLOR = (By.ID, f"{data}")

        return METRO_RENT, COLOR
