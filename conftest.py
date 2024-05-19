import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.order_page import OrderPage
from urls import Urls

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    home_page = HomePage(driver)
    home_page.go_to_site(Urls.URL_HOME)
    home_page.click_button_cookies()

    return home_page

@pytest.fixture
def order_page(driver):
    order_page = OrderPage(driver)

    return order_page
