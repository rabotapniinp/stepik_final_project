from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "There is product in the basket"

    def should_be_empty_basket_message(self):
        assert 'empty' in self.browser.find_element(By.CSS_SELECTOR, 'p').text, "Basket is not empty"  # (By.XPATH, "//p[contains(text(), 'empty')]")
