from PythonPytestHomework435.Selenium_commands.POM.tests.base_test import BaseTest


class TestFFofArmeniaPageFunctionality(BaseTest):
    def test_ffarmenia_page_national_team_history_text_availability(self):
        self.navigate_to_football_federation_of_armenia_page_and_check_natteamhistory_text()
