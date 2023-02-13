
import time
from .base_page import BasePage
from .locators import BasketPageLocators

url = "http://selenium1py.pythonanywhere.com/basket/"


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT_FORM, 2), "\nBasket content form is present"
        return True

    def remove_all_items_from_basket(self):
        try:
            self.basket_should_be_empty()
            print("There is no items in the basket")
        except AssertionError:
            input_quantity_locators = self.wait_elements(*BasketPageLocators.GROUP_INPUTS_ITEM_QUANTITY)
            for input_quantity in input_quantity_locators:
                self.actChain.scroll_to_element(input_quantity)
                input_quantity.clear()
                input_quantity.send_keys("0")
                time.sleep(0.1)
            updateQuantityButton = self.wait_elements(*BasketPageLocators.GROUP_BUTTONS_UPDATE_ITEM_QUANTITY)[0]
            updateQuantityButton.click()

    def should_be_basket_url(self):
        currentURL = self.browser.current_url
        assert "basket" in currentURL, r"There is no /basket in current URL"
        return True

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        emptyBasketMessage = self.wait_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        assert emptyBasketMessage.text == "Your basket is empty. Continue shopping",\
            f"\nText message doesn't compare '{emptyBasketMessage.text}'"
        return True




