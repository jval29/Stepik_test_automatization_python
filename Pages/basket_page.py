
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT_FORM, 2), "\nBasket content form is present"
        return True

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




