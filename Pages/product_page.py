
import time
import re
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_to_cart(self):
        addButton = self.wait_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        addButton.click()

    def should_be_success_message(self, productName):
        message = self.wait_element(*ProductPageLocators.SUCCESS_MESSAGE, 8)
        assert message.text.lower() == f"{productName} has been added to your basket.", "\nText message doesn't compare"
        return True

    def should_not_be_success_message(self, timeout):
        message = self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE, timeout)
        assert message, "\nSuccess message is present"
        return True

    def should_be_equal_amount_in_cart(self, productPrice, lastAmount):
        time.sleep(1)
        self.check_document_state()
        actualCartAmount = self.wait_element(*ProductPageLocators.AMOUNT_IN_CART)
        actualCartAmount = re.search(r"\d+[.,]\d\d", actualCartAmount.text)[0]
        calcNewCartAmount = str(round((float(lastAmount) + float(productPrice)), 2))
        assert actualCartAmount == calcNewCartAmount, \
            f"\nProduct price + last cart amount({productPrice}+{lastAmount}={calcNewCartAmount})" \
            f" and a new cart amount({actualCartAmount}) doesn't equal"
        return True
