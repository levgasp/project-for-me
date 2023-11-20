from selenium.webdriver.common.by import By
from PythonPytestHomework435.Selenium_commands.POM.lib.helpers import Helpers


class HomePage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)

    national_associations_loc = (By.LINK_TEXT, 'National Associations')

    def click_on_national_associations_section(self):
        self.find_and_click(self.national_associations_loc)
