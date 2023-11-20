import pytest


@pytest.mark.usefixtures("get_driver")
class BaseTest:
    def navigate_to_football_federation_of_armenia_page_and_check_natteamhistory_text(self):
        self.homepage.click_on_national_associations_section()
        self.nationalassociationspage.click_on_football_federation_of_armenia_part()
        self.footballfederationpage.assert_national_team_history_text()
