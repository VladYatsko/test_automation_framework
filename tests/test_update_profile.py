import allure
from locators.home_locators import HomePageLocators
from locators.register_locators import RegisterPageLocators
from locators.update_profile_locators import UpdatedProfileLocators
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.update_profile_page import UpdateProfilePage


class TestUpdateProfile:
    @allure.title("Validation that user is able to update profile data.")
    def test_update_profile_with_proper_data(self, driver):
        with allure.step('Proceed to home page.'):
            home_page = HomePage(driver, HomePageLocators.URL)
            home_page.open_page()
        with allure.step('Validation that home page is opened.'):
            home_page.home_page_is_expected()
        with allure.step('Proceed to registration page.'):
            home_page.proceed_to_registration()
        with allure.step('Validation that registration page is opened.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.register_page_is_expected()
        with allure.step('Specify all the fields and click submit button.'):
            register_page.full_register()
        with allure.step('Proceed to update profile page.'):
            update_profile = UpdateProfilePage(driver, UpdatedProfileLocators.URL)
            update_profile.open_page()
        with allure.step('Validation that update profile page is opened.'):
            update_profile.update_profile_page_is_expected()
        with allure.step('Specify first name.'):
            update_profile.specify_first_name()
        with allure.step('Specify last name.'):
            update_profile.specify_last_name()
        with allure.step('Click address.'):
            update_profile.specify_address()
        with allure.step('Click city.'):
            update_profile.specify_city()
        with allure.step('Click state.'):
            update_profile.specify_state()
        with allure.step('Click zip code.'):
            update_profile.specify_zip_code()
        with allure.step('Click submit button.'):
            update_profile.shift_from_element()
            update_profile.shift_from_element()
            update_profile.submit_by_keyboard()
        with allure.step('Validation that profile is successfully updated.'):
            update_profile.is_successful()
        