from selenium.webdriver.common.by import By

from PythonPytestHomework435.Selenium_commands.POM.lib.helpers import Helpers


class NationalAssociations(Helpers):
    def __init__(self, driver):
        super().__init__(driver)

    # football_federation_of_armenia_loc = (By.XPATH, '(//*[@slot="primary"])[4]')
    football_federation_of_armenia_loc = (By.XPATH, '(//*[@slot="prefix"])[4]')

    def click_on_football_federation_of_armenia_part(self):
        self.find_and_click(self.football_federation_of_armenia_loc)