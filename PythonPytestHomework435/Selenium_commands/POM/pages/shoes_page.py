# from hamcrest import equal_to

from selenium.webdriver.common.by import By
from PythonPytestHomework435.Selenium_commands.POM.lib.helpers import Helpers


class ShoesPage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)

    best_sellers_btn = (By.CLASS_NAME, 'nga-z')

    def click_on_best_sellers_btn(self):
        best_sellers_btn_txt = self.find(self.best_sellers_btn, get_text=True)
        assert best_sellers_btn_txt == "SHOP ALL WOMEN’S BEST SELLING SHOES"
        self.find_and_click(self.best_sellers_btn)
