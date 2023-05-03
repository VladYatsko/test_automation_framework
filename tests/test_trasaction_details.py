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


@allure.suite('Transaction details page test suit.')
class TestTransactionDetails:
    @allure.title("Validation that transaction details are displayed if user gets in.")
    def test_transaction_element_presence(self, driver):
        with allure.step('Proceed to register page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
            register_page.register_page_is_expected()
        register_page.full_register()
        with allure.step('Proceed to open account page.'):
            open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
            open_account.open_page()
            open_account.open_account_page_is_expected()
        with allure.step('Proceed to bill pay page.'):
            open_account.proceed_to_bill_pay()
            bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
        bill_pay_page.specify_all_the_fields_and_submit()
        bill_pay_page.is_successful()
        with allure.step('Proceed to account overview page and get into account.'):
            bill_pay_page.proceed_to_accounts_overview()
            account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
            account_overview.account_overview_page_is_expected()
            account_overview.get_into_account()
            account_activity = AccountActivityPage(driver, AccountActivityLocators.URL)
        with allure.step('Specify current month, click search.'):
            account_activity.select_month(datetime.datetime.now().strftime("%B"))
            account_activity.search_for_activity()
        account_activity.select_activity()
        with allure.step('Validation tha user is redirected to transaction details page.'):
            transaction_details = TransactionDetailsPage(driver, TransactionDetailsLocators.URL)
            assert account_activity.get_url() == TransactionDetailsLocators.URL\
                   + transaction_details.get_transaction_id()
