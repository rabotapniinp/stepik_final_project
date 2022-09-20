from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_added_to_basket_by_name(self):
        # проверка, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который действительно добавили
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING)
        assert product.text == message.text, 'Product name not found in basket'
        print(product, message)

    def should_be_added_to_basket_by_price(self):
        # проверка, что стоимость корзины совпадает с ценой товара
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_cost = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL)
        assert basket_cost.text == product_price.text, 'Basket cost not match the product price'
        print(product_price, basket_cost)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but must disappear"
