import allure

from selenium.webdriver.common.keys import Keys
from page_objects.page_objects import LogInObjects
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        @allure.step("Opening login page")
        def open_login_page(self):
            self.driver.find_element(*LogInObjects.login_link).click()

        @allure.step("Login with email: '1'")
        def set_user_inputs(self, email, password):
            self.driver.find_element(*LogInObjects.email_input).click()
            self.driver.find_element(*LogInObjects.email_input).send_keys(email)
            self.driver.find_element(*LogInObjects.password_input).click()
            self.driver.find_element(*LogInObjects.password_input).send_keys(password, Keys.ENTER)
            