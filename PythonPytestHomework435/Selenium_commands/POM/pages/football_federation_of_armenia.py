from selenium.webdriver.common.by import By

from PythonPytestHomework435.Selenium_commands.POM.lib.assertions import assert_that
from PythonPytestHomework435.Selenium_commands.POM.lib.helpers import Helpers


class FFofArmenia(Helpers):
    national_team_history_loc = (By.LINK_TEXT, 'National team history')

    def assert_national_team_history_text(self):
        actual_result = self.find(self.national_team_history_loc, timeout=10, get_text=True)
        expected_result = "National team history"
        assert_that(actual_result, expected_result)
