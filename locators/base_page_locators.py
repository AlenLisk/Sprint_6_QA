from selenium.webdriver.common.by import By


class BasePageLocators:

    ORDER_BUTTON_TOP = (By.XPATH, ".//button[@class='Button_Button__ra12g' and text()='Заказать']")
    BUTTON_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    BUTTON_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")