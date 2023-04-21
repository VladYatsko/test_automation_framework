import allure
from locators.account_activity_locators import AccountActivityLocators
from locators.account_overview_locators import AccountOverviewLocators
from locators.bill_pay_locators import BillPayLocators
from locators.open_account_locators import OpenAccountLocators
from locators.register_locators import RegisterPageLocators
from pages.account_overview_page import AccountOverviewPage
from pages.bill_pay_page import BillPayPage
from pages.open_account_page import OpenAccountPage
from pages.register_page import RegisterPage


class TestBillPage:
    @allure.title("Validation that payment can't be performed with no arguments.")
    def test_payment_with_no_arguments(self, driver):
        with allure.step('Proceed to registration page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
        with allure.step('Validation that register page is opened.'):
            register_page.register_page_is_expected()
        with allure.step('Specify all the fields and click submit button.'):
            register_page.full_register()
        with allure.step('Proceed to bill pay page.'):
            bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
            bill_pay_page.open_page()
        with allure.step('Click send payment button.'):
            bill_pay_page.move_to_element_and_submit(BillPayLocators.SEND_PAYMENT_BTN)
        with allure.step('Validation that informative messages are displayed.'):
            assert bill_pay_page.find_visible_element(BillPayLocators.ERROR_MSG).is_displayed() is True
   
    @allure.title("Validation that payment can be performed with proper input.")
    def test_payment_with_proper_data(self, driver):
        with allure.step('Proceed to registration page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
        with allure.step('Validation that register page is opened.'):
            register_page.register_page_is_expected()
        with allure.step('Specify all the fields and click submit button.'):
            register_page.full_register()
        with allure.step('Proceed to account overview page.'):
            account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
            account_overview.open_page()
        old_balance = float(account_overview.get_balance())
        with allure.step('Proceed to bill pay page.'):
            account_overview.proceed_to_bill_pay()
            bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
        with allure.step('Specify payee name.'):
            bill_pay_page.specify_first_name()
        with allure.step('Specify address.'):
            bill_pay_page.specify_address()
        with allure.step('Specify city.'):
            bill_pay_page.specify_city()
        with allure.step('Specify state.'):
            bill_pay_page.specify_state()
        with allure.step('Specify zip code.'):
            bill_pay_page.specify_zip_code()
        with allure.step('Specify phone number.'):
            bill_pay_page.specify_phone_num()
        with allure.step('Specify account and verify it.'):
            bill_pay_page.specify_account_and_verify()
        with allure.step('Specify amount.'):
            amount_to_send = bill_pay_page.specify_amount()
        with allure.step('Click send payment.'):
            bill_pay_page.send_payment()
        with allure.step('Validation that payment was successfully sent.'):
            bill_pay_page.is_successful()
        with allure.step('Proceed to account overview page.'):
            bill_pay_page.proceed_to_accounts_overview()
        with allure.step('Validation that account overview page is opened.'):
            account_overview.account_overview_page_is_expected()
        new_balance = float(account_overview.get_balance())
        with allure.step('Validation that current balance is less on amount which was payed.'):
            assert new_balance == old_balance - float(amount_to_send)
    
    @allure.title("Validation that payment can be performed from newly created bank account")
    def test_payment_from_another_account(self, driver):
        with allure.step('Proceed to registration page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
        with allure.step('Validation that register page is opened.'):
            register_page.register_page_is_expected()
        with allure.step('Specify all the fields and click submit button.'):
            register_page.full_register()
        with allure.step('Proceed to open account page.'):
            open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
            open_account.open_page()
        with allure.step('Select "Checking" account type.'):
            open_account.select_checking()
        with allure.step('Select account from which to create a new one.'):
            open_account.select_account()
        with allure.step('Click Submit button.'):
            open_account.submit_creation()
        with allure.step('Proceed to account overview page.'):
            account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
            account_overview.open_page()
        old_balance = float(account_overview.get_balance_by_index(1))
        with allure.step('Proceed to bill pay page.'):
            account_overview.proceed_to_bill_pay()
            bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
        with allure.step('Specify payee name.'):
            bill_pay_page.specify_first_name()
        with allure.step('Specify address.'):
            bill_pay_page.specify_address()
        with allure.step('Specify city.'):
            bill_pay_page.specify_city()
        with allure.step('Specify state.'):
            bill_pay_page.specify_state()
        with allure.step('Specify zip code.'):
            bill_pay_page.specify_zip_code()
        with allure.step('Specify phone number.'):
            bill_pay_page.specify_phone_num()
        with allure.step('Specify account and verify it.'):
            bill_pay_page.specify_account_and_verify()
        with allure.step('Specify amount.'):
            amount_to_send = bill_pay_page.specify_amount()
        with allure.step('Switch account to newly created one.'):
            bill_pay_page.select_another_account(1)
        with allure.step('Click send payment.'):
            bill_pay_page.send_payment()
        with allure.step('Validation that payment was successfully sent.'):
            bill_pay_page.is_successful()
        with allure.step('Proceed to account overview page.'):
            bill_pay_page.proceed_to_accounts_overview()
        with allure.step('Validation that account overview page is opened.'):
            account_overview.account_overview_page_is_expected()
        new_balance = float(account_overview.get_balance_by_index(1))
        with allure.step('Validation that current balance for new account is less on amount which was payed.'):
            assert new_balance == old_balance - float(amount_to_send)
        with allure.step('Click on existing account id.'):
            account_overview.get_into_account_by_index(1)
        with allure.step('Validation that user is redirected to details of existing account.'):
            assert AccountActivityLocators.URL in account_overview.get_url()
    