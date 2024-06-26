from conftest import *
from data import OrderDetails
import allure
from urls import Urls


class TestOrderPage:

        @pytest.mark.parametrize(
                "data",
                [
                        (OrderDetails.data_1),
                        (OrderDetails.data_2)
                ]
        )
        @allure.title('Проверка оформления заказа с разными данными')
        @allure.description('При корректном заполнении форм заказ успешно оформляется')
        def test_set_an_order(self, home_page, order_page, data):
                home_page.click_order_button_top()
                order_page.fill_form_personal_info(data)
                order_page.fill_form_rent_info(data)

                assert 'Заказ оформлен' in order_page.get_modal_window_text()

        @allure.title('Проверка нажатия на лого Самокат')
        @allure.description('При нажатии на лого Самокат происходит переход на глаааавную страницу Самоката')
        def test_button_scooter(self, order_page):
                order_page.go_to_site(Urls.URL_ORDER)
                expected_url = Urls.URL_HOME

                order_page.click_scooter_button()
                actual_url = order_page.get_current_url()

                assert actual_url == expected_url
