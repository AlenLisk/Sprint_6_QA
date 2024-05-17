from selenium.webdriver.common.by import By

class HomePageLocators:

    QUESTIONS_ABOUT_IMPORTANT = (By.XPATH, ".//div[text()='Вопросы о важном']")
    COOKIES_BUTTON = (By.XPATH, ".//button[text()='да все привыкли']")

    @staticmethod
    def question_locator_generator(number_question):
        QUESTION = (By.ID, f'accordion__heading-{number_question}')
        ANSWER = (By.ID, f'accordion__panel-{number_question}')

        return QUESTION, ANSWER


    ORDER_BUTTON_CENTER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    MODAL_COOKIES = (By.CLASS_NAME, "App_CookieText__1sbqp")
