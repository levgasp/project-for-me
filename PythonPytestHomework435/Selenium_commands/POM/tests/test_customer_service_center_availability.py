from PythonPytestHomework435.Selenium_commands.POM.tests.base_test import BaseTest


class TestCustomerServiceText(BaseTest):
    def test_text_customer_service_center(self):
        self.navigate_customer_service_center_page_and_check_appropriate_text()