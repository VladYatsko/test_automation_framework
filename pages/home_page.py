from locators.home_locators import HomePageLocators
from pages.base_page import BasePage
from generator.generator import generated_data


class HomePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        
    def home_page_is_expected(self) -> None:
        assert self.get_url() == HomePageLocators.URL
    
    def input_username(self) -> None:
        created_data = next(generated_data())
        return self.send_text(HomePageLocators.USER_NAME, created_data.username)
    
    def input_password(self) -> None:
        created_data = next(generated_data())
        return self.send_text(HomePageLocators.PASSWORD, created_data.password)
    
    def submit_login(self) -> None:
        self.click_element(HomePageLocators.LOG_IN)
    
    def proceed_to_registration(self) -> None:
        self.click_element(HomePageLocators.REGISTER_TRANSITION)
        
    def proceed_to_customer_care(self) -> None:
        self.click_element(HomePageLocators.CUSTOMER_CARE_TRANSITION)
        