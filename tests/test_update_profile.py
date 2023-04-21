from locators.home_locators import HomePageLocators
from locators.register_locators import RegisterPageLocators
from locators.update_profile_locators import UpdatedProfileLocators
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.update_profile_page import UpdateProfilePage


class TestUpdateProfile:
    def test_update_profile_with_proper_data(self, driver):
        home_page = HomePage(driver, HomePageLocators.URL)
        home_page.open_page()
        home_page.home_page_is_expected()
        home_page.proceed_to_registration()
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.register_page_is_expected()
        register_page.full_register()
        update_profile = UpdateProfilePage(driver, UpdatedProfileLocators.URL)
        update_profile.open_page()
        update_profile.update_profile_page_is_expected()
        update_profile.specify_first_name()
        update_profile.specify_last_name()
        update_profile.is_successful()
        