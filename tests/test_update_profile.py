import allure
from locators.home_locators import HomePageLocators
from locators.register_locators import RegisterPageLocators
from locators.update_profile_locators import UpdatedProfileLocators
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.update_profile_page import UpdateProfilePage


@allure.suite('Update profile page test suit.')
class TestUpdateProfile:
    @allure.title("Validation that user is able to update profile data.")
    def test_update_profile_with_proper_data(self, driver):
        with allure.step('Proceed to home page.'):
            home_page = HomePage(driver, HomePageLocators.URL)
            home_page.open_page()
            home_page.home_page_is_expected()
        with allure.step('Proceed to register page.'):
            home_page.proceed_to_registration()
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.register_page_is_expected()
        register_page.full_register()
        with allure.step('Proceed to update profile page.'):
            update_profile = UpdateProfilePage(driver, UpdatedProfileLocators.URL)
            update_profile.open_page()
            update_profile.update_profile_page_is_expected()
        with allure.step('specify the fields and submit.'):
            update_profile.specify_first_name()
            update_profile.specify_last_name()
            update_profile.specify_address()
            update_profile.specify_city()
            update_profile.specify_state()
            update_profile.specify_zip_code()
            update_profile.shift_from_element()
            update_profile.shift_from_element()
            update_profile.submit_by_keyboard()
        update_profile.is_successful()
