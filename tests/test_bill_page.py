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


@allure.suite('Bill pay page test suit.')
class TestBillPage:
    @allure.title("Validation that payment can't be performed with no arguments.")
    def test_payment_with_no_arguments(self, driver):
        with allure.step('Proceed to register page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
            register_page.register_page_is_expected()
        register_page.full_register()
        with allure.step('Proceed to bill pay page.'):
            bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
            bill_pay_page.open_page()
        with allure.step('Click submit button.'):
            bill_pay_page.move_to_element_and_submit(BillPayLocators.SEND_PAYMENT_BTN)
        with allure.step('Validation that informative messages are displayed.'):
            assert bill_pay_page.find_visible_element(BillPayLocators.ERROR_MSG).is_displayed() is True
   
    @allure.title("Validation that payment can be performed with proper input.")
    def test_payment_with_proper_data(self, driver):
        with allure.step('Proceed to register page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
            register_page.register_page_is_expected()
        register_page.full_register()
        with allure.step('Proceed to account overview page and get balance.'):
            account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
            account_overview.open_page()
            old_balance = float(account_overview.get_balance())
        with allure.step('Proceed to bill pay page.'):
            account_overview.proceed_to_bill_pay()
        with allure.step('Specify all the fields and click submit'):
            bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
            bill_pay_page.specify_first_name()
            bill_pay_page.specify_address()
            bill_pay_page.specify_city()
            bill_pay_page.specify_state()
            bill_pay_page.specify_zip_code()
            bill_pay_page.specify_phone_num()
            bill_pay_page.specify_account_and_verify()
            amount_to_send = bill_pay_page.specify_amount()
            bill_pay_page.send_payment()
        bill_pay_page.is_successful()
        with allure.step('Proceed to account overview page and get updated balance.'):
            bill_pay_page.proceed_to_accounts_overview()
            account_overview.account_overview_page_is_expected()
            new_balance = float(account_overview.get_balance())
        with allure.step('Validation that current balance is less on amount which was payed.'):
            assert new_balance == old_balance - float(amount_to_send)
    
    @allure.title("Validation that payment can be performed from newly created bank account")
    def test_payment_from_another_account(self, driver):
        with allure.step('Proceed to register page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
            register_page.register_page_is_expected()
        register_page.full_register()
        with allure.step('Proceed to open account page.'):
            open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
            open_account.open_page()
        with allure.step('Create account of "Checking" type.'):
            open_account.select_checking()
            open_account.select_account()
            open_account.submit_creation()
        with allure.step('Proceed to account overview page and get balance.'):
            account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
            account_overview.open_page()
            old_balance = float(account_overview.get_balance_by_index(1))
        with allure.step('Proceed to bill pay page.'):
            account_overview.proceed_to_bill_pay()
        with allure.step('Specify all the fields and click submit.'):
            bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
            bill_pay_page.specify_first_name()
            bill_pay_page.specify_address()
            bill_pay_page.specify_city()
            bill_pay_page.specify_state()
            bill_pay_page.specify_zip_code()
            bill_pay_page.specify_phone_num()
            bill_pay_page.specify_account_and_verify()
            amount_to_send = bill_pay_page.specify_amount()
            bill_pay_page.select_another_account(1)
            bill_pay_page.send_payment()
        bill_pay_page.is_successful()
        with allure.step('Proceed to account overview page and get updated balance.'):
            bill_pay_page.proceed_to_accounts_overview()
            account_overview.account_overview_page_is_expected()
            new_balance = float(account_overview.get_balance_by_index(1))
        with allure.step('Validation that current balance for new account is less on amount which was payed.'):
            assert new_balance == old_balance - float(amount_to_send)
        account_overview.get_into_account_by_index(1)
        with allure.step('Validation that user is redirected to details of existing account.'):
            assert AccountActivityLocators.URL in account_overview.get_url()
    