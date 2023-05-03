import allure
from locators.home_locators import HomePageLocators
from pages.base_page import BasePage
from generator.generator import generated_data


class HomePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
    
    @allure.step('Validation that home page is opened.')
    def home_page_is_expected(self) -> None:
        assert HomePageLocators.URL in self.get_url()
    
    @allure.step('Specify username.')
    def input_username(self) -> str:
        created_data = next(generated_data())
        return self.send_text(HomePageLocators.USER_NAME, created_data.username)
    
    @allure.step('Specify password.')
    def input_password(self) -> str:
        created_data = next(generated_data())
        return self.send_text(HomePageLocators.PASSWORD, created_data.password)
    
    @allure.step('Click login button.')
    def submit_login(self) -> None:
        self.click_element(HomePageLocators.LOG_IN)
    
    @allure.step('Proceed to register page.')
    def proceed_to_registration(self):
        self.click_element(HomePageLocators.REGISTER_TRANSITION)
    
    @allure.step('Proceed to customer care page.')
    def proceed_to_customer_care(self):
        self.click_element(HomePageLocators.CUSTOMER_CARE_TRANSITION)
        