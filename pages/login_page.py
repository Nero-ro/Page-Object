from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_url(self):
        assert ('login' in self.browser.current_url), "Login URL does not contains 'login' word."

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found."

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not found."