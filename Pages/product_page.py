import re
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        addButton = self.wait_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        self.move_n_click(addButton)

    def should_be_added_message(self, productName):
        message = self.wait_element(*ProductPageLocators.MESSAGE_WAS_ADDED)
        assert message.text.lower() == f"{productName} has been added to your basket.", "Text message doesn't compare"

    def should_be_equal_amount_in_cart(self, productPrice, lastAmount):
        cartAmount = self.wait_element(*ProductPageLocators.AMOUNT_IN_CART)
        cartAmount = re.search(r"\d+[.,]\d\d", cartAmount.text)[0]
        assert float(cartAmount) == float(lastAmount)+float(productPrice), "Product price and Cart amount doesn't equal"
