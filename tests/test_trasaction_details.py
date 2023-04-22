import allure
from locators.account_activity_locators import AccountActivityLocators
from locators.account_overview_locators import AccountOverviewLocators
from locators.bill_pay_locators import BillPayLocators
from locators.open_account_locators import OpenAccountLocators
from locators.register_locators import RegisterPageLocators
from locators.transaction_details_locators import TransactionDetailsLocators
from pages.account_activity_page import AccountActivityPage
from pages.account_overview_page import AccountOverviewPage
from pages.bill_pay_page import BillPayPage
from pages.open_account_page import OpenAccountPage
from pages.register_page import RegisterPage
import datetime
from pages.transaction_details_page import TransactionDetailsPage


class TestTransactionDetails:
    @allure.title("Validation that transaction details are displayed if user gets in.")
    def test_transaction_element_presence(self, driver):
        with allure.step('Proceed to registration page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
        with allure.step('Validation that registration page is opened.'):
            register_page.register_page_is_expected()
        with allure.step('Specify all the fields and click submit button.'):
            register_page.full_register()
        with allure.step('Proceed to open account page.'):
            open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
            open_account.open_page()
        with allure.step('Validation that open account page is opened.'):
            open_account.open_account_page_is_expected()
        with allure.step('Proceed to bill pay page.'):
            open_account.proceed_to_bill_pay()
        with allure.step('Specify all the fields and send payment.'):
            bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
            bill_pay_page.specify_all_the_fields_and_submit()
        with allure.step('Validation that payment is successful.'):
            bill_pay_page.is_successful()
        with allure.step('Proceed to accounts overview page.'):
            bill_pay_page.proceed_to_accounts_overview()
        with allure.step('Validation that account overview page is opened.'):
            account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
            account_overview.account_overview_page_is_expected()
        with allure.step('Click on existing account id.'):
            account_overview.get_into_account()
        with allure.step('Specify current month.'):
            account_activity = AccountActivityPage(driver, AccountActivityLocators.URL)
            account_activity.select_month(datetime.datetime.now().strftime("%B"))
        with allure.step('Click Search button.'):
            account_activity.search_for_activity()
        with allure.step('Click on transaction id.'):
            account_activity.select_activity()
        with allure.step('Validation tha user is redirected to transaction details page.'):
            transaction_details = TransactionDetailsPage(driver, TransactionDetailsLocators.URL)
            assert account_activity.get_url() == TransactionDetailsLocators.URL + transaction_details.get_transaction_id()
        