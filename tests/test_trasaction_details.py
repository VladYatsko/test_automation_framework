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
    def test_transaction_element_presence(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.open_page()
        register_page.register_page_is_expected()
        register_page.full_register()
        open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
        open_account.open_page()
        open_account.open_account_page_is_expected()
        open_account.proceed_to_bill_pay()
        bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
        bill_pay_page.specify_first_name()
        bill_pay_page.specify_address()
        bill_pay_page.specify_city()
        bill_pay_page.specify_state()
        bill_pay_page.specify_zip_code()
        bill_pay_page.specify_phone_num()
        bill_pay_page.specify_account_and_verify()
        bill_pay_page.specify_amount()
        bill_pay_page.send_payment()
        bill_pay_page.is_successful()
        bill_pay_page.proceed_to_accounts_overview()
        account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
        account_overview.account_overview_page_is_expected()
        account_overview.get_into_account()
        account_activity = AccountActivityPage(driver, AccountActivityLocators.URL)
        account_activity.select_month(datetime.datetime.now().strftime("%B"))
        account_activity.search_for_activity()
        account_activity.select_activity()
        transaction_details = TransactionDetailsPage(driver, TransactionDetailsLocators.URL)
        assert account_activity.get_url() == TransactionDetailsLocators.URL + transaction_details.get_transaction_id()
        