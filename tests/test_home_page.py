from locators.customer_care_locators import CustomerCarePageLocators
from locators.home_locators import HomePageLocators
from locators.open_account_locators import OpenAccountLocators
from locators.register_locators import RegisterPageLocators
from pages.customer_care_page import CustomerCarePage
from pages.home_page import HomePage
from pages.open_account_page import OpenAccountPage
from pages.register_page import RegisterPage


class TestHomePage:
    def test_unregistered_log_in(self, driver):
        home_page = HomePage(driver, HomePageLocators.URL)
        home_page.open_page()
        home_page.input_username()
        home_page.input_password()
        home_page.submit_login()
        assert home_page.find_presenting_element(HomePageLocators.ERROR_MSG).is_displayed() is True
        
    def test_login_without_password(self, driver):
        home_page = HomePage(driver, HomePageLocators.URL)
        home_page.open_page()
        home_page.input_username()
        home_page.submit_login()
        assert home_page.find_presenting_element(HomePageLocators.ERROR_MSG).is_displayed() is True
        
    def test_login_without_username(self, driver):
        home_page = HomePage(driver, HomePageLocators.URL)
        home_page.open_page()
        home_page.input_password()
        home_page.submit_login()
        assert home_page.find_presenting_element(HomePageLocators.ERROR_MSG).is_displayed() is True
    
    def test_redirection_between_pages(self, driver):
        home_page = HomePage(driver, HomePageLocators.URL)
        home_page.open_page()
        home_page.proceed_to_registration()
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.register_page_is_expected()
        register_page.return_back()
        home_page.proceed_to_customer_care()
        customer_care = CustomerCarePage(driver, CustomerCarePageLocators.URL)
        customer_care.customer_care_page_is_expected()
        customer_care.return_back()
        home_page.home_page_is_expected()
    
    def test_registered_user_login(self, driver):
        home_page = HomePage(driver, HomePageLocators.URL)
        home_page.open_page()
        home_page.proceed_to_registration()
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.specify_first_name()
        register_page.specify_last_name()
        register_page.specify_address()
        register_page.specify_city()
        register_page.specify_state()
        register_page.specify_zip_code()
        register_page.specify_phone_number()
        register_page.specify_ssn()
        username = register_page.specify_user_name()
        password = register_page.specify_password()
        register_page.submit_register()
        open_account_page = OpenAccountPage(driver, OpenAccountLocators.URL)
        open_account_page.open_page()
        open_account_page.proceed_to_log_out()
        home_page.open_page()
        home_page.send_text(HomePageLocators.USER_NAME, username)
        home_page.send_text(HomePageLocators.PASSWORD, password)
        home_page.submit_login()
        open_account_page.open_page()
        open_account_page.open_account_page_is_expected()
    