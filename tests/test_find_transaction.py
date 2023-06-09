import datetime
from datetime import datetime
import random
import allure
from locators.account_activity_locators import AccountActivityLocators
from locators.account_overview_locators import AccountOverviewLocators
from locators.bill_pay_locators import BillPayLocators
from locators.find_transaction_locators import FindTransactionLocators
from locators.register_locators import RegisterPageLocators
from locators.transaction_details_locators import TransactionDetailsLocators
from pages.account_activity_page import AccountActivityPage
from pages.account_overview_page import AccountOverviewPage
from pages.bill_pay_page import BillPayPage
from pages.find_transaction_page import FindTransactionPage
from pages.register_page import RegisterPage
from pages.transaction_details_page import TransactionDetailsPage


@allure.suite('Find transaction page test suit.')
class TestFindTransaction:
    @allure.title("Validation that transaction can be found using existing transaction id.")
    def test_find_by_proper_id(self, driver):
        with allure.step('Proceed to register page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
            register_page.register_page_is_expected()
        register_page.full_register()
        with allure.step('Proceed to account overview page.'):
            account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
            account_overview.open_page()
        with allure.step('Proceed to bill pay page.'):
            account_overview.proceed_to_bill_pay()
        bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
        bill_pay_page.specify_all_the_fields_and_submit()
        bill_pay_page.is_successful()
        with allure.step('Proceed to account overview page.'):
            bill_pay_page.proceed_to_accounts_overview()
            account_overview.account_overview_page_is_expected()
        account_overview.get_into_account()
        account_activity = AccountActivityPage(driver, AccountActivityLocators.URL)
        with allure.step('Specify month, click search and click on activity.'):
            account_activity.select_month(datetime.now().strftime("%B"))
            account_activity.search_for_activity()
            account_activity.select_activity()
            transaction_details = TransactionDetailsPage(driver, TransactionDetailsLocators.URL)
            transaction_id = transaction_details.get_transaction_id()
        with allure.step('Proceed to find transaction page.'):
            transaction_details.proceed_to_find_transactions()
            find_transaction = FindTransactionPage(driver, FindTransactionLocators.URL)
            find_transaction.find_transaction_page_is_expected()
        with allure.step('Specify transaction ID and submit.'):
            find_transaction.specify_transaction_id(transaction_id)
            find_transaction.submit_by_transaction_id()
        find_transaction.is_successful()
    
    @allure.title("Validation that transaction can't be found by incorrect transaction id number.")
    def test_find_by_incorrect_id(self, driver):
        with allure.step('Proceed to register page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
            register_page.register_page_is_expected()
        register_page.full_register()
        with allure.step('Proceed to account overview page.'):
            account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
            account_overview.open_page()
        with allure.step('Proceed to find transaction page.'):
            account_overview.proceed_to_find_transactions()
            find_transaction = FindTransactionPage(driver, FindTransactionLocators.URL)
            find_transaction.find_transaction_page_is_expected()
        with allure.step('Specify random transaction ID and submit.'):
            find_transaction.specify_transaction_id(random.randint(10000, 100000))
            find_transaction.submit_by_transaction_id()
        find_transaction.is_not_successful()
    
    @allure.title("Validation that transaction can't be found if id field is empty.")
    def test_find_with_empty_id(self, driver):
        with allure.step('Proceed to register page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
            register_page.register_page_is_expected()
        register_page.full_register()
        with allure.step('Proceed to account overview page.'):
            account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
            account_overview.open_page()
        with allure.step('Proceed to find transaction page.'):
            account_overview.proceed_to_find_transactions()
            find_transaction = FindTransactionPage(driver, FindTransactionLocators.URL)
            find_transaction.find_transaction_page_is_expected()
        find_transaction.submit_by_transaction_id()
        with allure.step('Validation that search was not initiated.'):
            assert find_transaction.find_visible_element(FindTransactionLocators.REQUIRED).is_displayed() is True
    
    @allure.title("Validation that user can find transaction by date.")
    def test_find_by_proper_date(self, driver):
        with allure.step('Proceed to register page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
            register_page.register_page_is_expected()
        register_page.full_register()
        with allure.step('Proceed to account overview page.'):
            account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
            account_overview.open_page()
        with allure.step('Proceed to bill pay page.'):
            account_overview.proceed_to_bill_pay()
            bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
        bill_pay_page.specify_all_the_fields_and_submit()
        bill_pay_page.is_successful()
        with allure.step('Proceed to find transaction page.'):
            bill_pay_page.proceed_to_find_transactions()
            find_transaction = FindTransactionPage(driver, FindTransactionLocators.URL)
            find_transaction.find_transaction_page_is_expected()
        with allure.step('Specify date and submit.'):
            find_transaction.specify_date()
            find_transaction.submit_by_date()
        find_transaction.is_successful()
    
    @allure.title("Validation that user can find transaction by proper date range.")
    def test_find_by_correct_date_range(self, driver):
        with allure.step('Proceed to register page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
            register_page.register_page_is_expected()
        register_page.full_register()
        with allure.step('Proceed to account overview page.'):
            account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
            account_overview.open_page()
        with allure.step('Proceed to bill pay page.'):
            account_overview.proceed_to_bill_pay()
            bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
        bill_pay_page.specify_all_the_fields_and_submit()
        bill_pay_page.is_successful()
        with allure.step('Proceed to find transaction page.'):
            bill_pay_page.proceed_to_find_transactions()
            find_transaction = FindTransactionPage(driver, FindTransactionLocators.URL)
            find_transaction.find_transaction_page_is_expected()
        with allure.step('Specify date range and submit.'):
            find_transaction.specify_range_start('04-20-2023')
            find_transaction.specify_range_end(datetime.today().strftime('%m-%d-%Y'))
            find_transaction.submit_by_range()
        find_transaction.is_successful()
    
    @allure.title("Validation that user can find transaction by amount value.")
    def test_find_by_proper_amount(self, driver):
        with allure.step('Proceed to register page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
            register_page.register_page_is_expected()
        register_page.full_register()
        with allure.step('Proceed to account overview page.'):
            account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
            account_overview.open_page()
        with allure.step('Proceed to bill pay page.'):
            account_overview.proceed_to_bill_pay()
            bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
        with allure.step('Specify all the fields and click submit.'):
            bill_pay_page.specify_first_name()
            bill_pay_page.specify_address()
            bill_pay_page.specify_city()
            bill_pay_page.specify_state()
            bill_pay_page.specify_zip_code()
            bill_pay_page.specify_phone_num()
            bill_pay_page.specify_account_and_verify()
            amount = bill_pay_page.specify_amount()
            bill_pay_page.send_payment()
        bill_pay_page.is_successful()
        with allure.step('Proceed to find transaction page.'):
            bill_pay_page.proceed_to_find_transactions()
            find_transaction = FindTransactionPage(driver, FindTransactionLocators.URL)
            find_transaction.find_transaction_page_is_expected()
        with allure.step('Specify date range and submit.'):
            find_transaction.specify_amount(amount)
            find_transaction.submit_amount()
        find_transaction.is_successful()
