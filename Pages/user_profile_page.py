
from .base_page import BasePage, BasePageLocators
from .locators import UserProfilePageLocators


class UserProfilePage(BasePage):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete_user_profile(self):
        currentEmail = self.wait_element(*UserProfilePageLocators.CURRENT_EMAIL).text.strip()
        deleteButton = self.wait_element(*UserProfilePageLocators.BUTTON_DELETE_PROFILE)
        deleteButton.click()
        inputConfirmPwd = self.wait_element(*UserProfilePageLocators.INPUT_DELETE_PWD_CONFIRM)
        email, __pwd = self.auth_get_data_json(currentEmail)
        inputConfirmPwd.send_keys(__pwd)
        confirmButton = self.wait_element(*UserProfilePageLocators.BUTTON_DELETE_PWD_SUBMIT)
        confirmButton.click()
        self.auth_remove_single_data_from_json(email)

    def should_be_user_profile_page(self):
        assert "profile" in self.browser.current_url, "\nCurrent url doesn't contain 'profile'"
        assert self.is_element_present(
            *UserProfilePageLocators.BUTTON_DELETE_PROFILE), "\nThere is no profile delete button"
        return True
