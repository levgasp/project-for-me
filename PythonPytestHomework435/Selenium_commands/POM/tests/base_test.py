import pytest


@pytest.mark.usefixtures("get_driver")
class BaseTest:
    def navigate_shoes_page_and_check_best_sellers_functionality(self):
        self.homepage.click_on_shoes_section()
        self.shoespage.click_on_best_sellers_btn()

    def navigate_customer_service_center_page_and_check_appropriate_text(self):
        self.homepage.click_on_customer_srv_cntr_section()
        self.customerservice_center_page.assert_header_on_customer_service_page()