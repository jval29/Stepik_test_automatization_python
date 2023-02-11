
import re
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_to_cart(self):
        addButton = self.wait_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        self.move_n_click(addButton)

    def should_be_success_message(self, productName):
        message = self.wait_element(*ProductPageLocators.SUCCESS_MESSAGE)
        assert message.text.lower() == f"{productName} has been added to your basket.", "\nText message doesn't compare"
        return True

    def should_not_be_success_message(self, timeout):
        message = self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE, timeout)
        assert message, "\nSuccess message is present"
        return True

    def should_be_equal_amount_in_cart(self, productPrice, lastAmount):
        cartAmount = self.wait_element(*ProductPageLocators.AMOUNT_IN_CART)
        cartAmount = re.search(r"\d+[.,]\d\d", cartAmount.text)[0]
        newCartAmount = str(round((float(lastAmount) + float(productPrice)), 2))
        assert cartAmount == newCartAmount, \
            f"\nProduct price + stored cart amount({productPrice}+{lastAmount}={newCartAmount})" \
            f" and a new cart amount({cartAmount}) doesn't equal"
        return True
