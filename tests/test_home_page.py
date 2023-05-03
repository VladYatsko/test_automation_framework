import allure
from locators.customer_care_locators import CustomerCarePageLocators
from locators.home_locators import HomePageLocators
from locators.open_account_locators import OpenAccountLocators
from locators.register_locators import RegisterPageLocators
from pages.customer_care_page import CustomerCarePage
from pages.home_page import HomePage
from pages.open_account_page import OpenAccountPage
from pages.register_page import RegisterPage


@allure.suite('Home page test suit.')
class TestHomePage:
    @allure.title("Validation that unregistered user can't get in.")
    def test_unregistered_log_in(self, driver):
        with allure.step('Proceed to home page.'):
            home_page = HomePage(driver, HomePageLocators.URL)
            home_page.open_page()
        with allure.step('Login with wrong username and password.'):
            home_page.input_username()
            home_page.input_password()
            home_page.submit_login()
        with allure.step('Validation that user is not logged in.'):
            assert home_page.find_visible_element(HomePageLocators.ERROR_MSG).is_displayed() is True
    
    @allure.title("Validation that user can't login without specifying password.")
    def test_login_without_password(self, driver):
        with allure.step('Proceed to home page.'):
            home_page = HomePage(driver, HomePageLocators.URL)
            home_page.open_page()
        with allure.step('Login without password.'):
            home_page.input_username()
            home_page.submit_login()
        with allure.step('Validation that user is not logged in.'):
            assert home_page.find_visible_element(HomePageLocators.ERROR_MSG).is_displayed() is True
    
    @allure.title("Validation that user can't login without specifying username.")
    def test_login_without_username(self, driver):
        with allure.step('Proceed to home page.'):
            home_page = HomePage(driver, HomePageLocators.URL)
            home_page.open_page()
        with allure.step('Login without username.'):
            home_page.input_password()
            home_page.submit_login()
        with allure.step('Validation that user is not logged in.'):
            assert home_page.find_visible_element(HomePageLocators.ERROR_MSG).is_displayed() is True
    
    @allure.title("Validation that user is able to redirect between pages.")
    def test_redirection_between_pages(self, driver):
        with allure.step('Open home page.'):
            home_page = HomePage(driver, HomePageLocators.URL)
            home_page.open_page()
        with allure.step('Proceed to registration page.'):
            home_page.proceed_to_registration()
        with allure.step('Validation that register page is opened'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.register_page_is_expected()
        with allure.step('Return back to home page.'):
            register_page.return_back()
        with allure.step('Proceed to customer care page.'):
            home_page.proceed_to_customer_care()
        with allure.step('Validation that customer care page is opened.'):
            customer_care = CustomerCarePage(driver, CustomerCarePageLocators.URL)
            customer_care.customer_care_page_is_expected()
        with allure.step('Return back to home page.'):
            customer_care.return_back()
        with allure.step('Validation that home page is opened.'):
            home_page.home_page_is_expected()
    
    @allure.title("Validation that existing user is able to log in.")
    def test_registered_user_login(self, driver):
        with allure.step('Proceed to home page.'):
            home_page = HomePage(driver, HomePageLocators.URL)
            home_page.open_page()
        with allure.step('Proceed to register page.'):
            home_page.proceed_to_registration()
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
        with allure.step('Specify all the fields and click register button.'):
            register_page.specify_first_name()
            register_page.specify_last_name()
            register_page.specify_address()
            register_page.specify_city()
            register_page.specify_state()
            register_page.specify_zip_code()
            register_page.specify_phone_number()
            register_page.specify_ssn()
            register_page.specify_user_name()
            register_page.specify_password()
            username = register_page.get_text(RegisterPageLocators.USERNAME)
            password = register_page.get_text(RegisterPageLocators.PASSWORD)
            register_page.submit_register()
        with allure.step('Proceed to open account page.'):
            open_account_page = OpenAccountPage(driver, OpenAccountLocators.URL)
            open_account_page.open_page()
        with allure.step('Logout.'):
            open_account_page.proceed_to_log_out()
        with allure.step('Proceed to home page.'):
            home_page.open_page()
        with allure.step('Login with existing credentials.'):
            home_page.send_text(HomePageLocators.USER_NAME, username)
            home_page.send_text(HomePageLocators.PASSWORD, password)
            home_page.submit_login()
        with allure.step('Proceed to open account page.'):
            open_account_page.open_page()
            open_account_page.open_account_page_is_expected()
