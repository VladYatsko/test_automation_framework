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


class TestFindTransaction:
    @allure.title("Validation that transaction can be found using existing transaction id.")
    def test_find_by_proper_id(self, driver):
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
        with allure.step('Proceed to bill pay page.'):
            account_overview.proceed_to_bill_pay()
            bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
        with allure.step('Specify all the fields and send payment.'):
            bill_pay_page.specify_all_the_fields_and_submit()
        with allure.step('Validation that payment was successfully sent.'):
            bill_pay_page.is_successful()
        with allure.step('Proceed to account overview page.'):
            bill_pay_page.proceed_to_accounts_overview()
        with allure.step('Validation that account overview page is opened.'):
            account_overview.account_overview_page_is_expected()
        with allure.step('Click on existing account id.'):
            account_overview.get_into_account()
        with allure.step('Specify current month.'):
            account_activity = AccountActivityPage(driver, AccountActivityLocators.URL)
            account_activity.select_month(datetime.now().strftime("%B"))
        with allure.step('Click Search button.'):
            account_activity.search_for_activity()
        with allure.step('Click on transaction id.'):
            account_activity.select_activity()
        with allure.step('Check transaction id.'):
            transaction_details = TransactionDetailsPage(driver, TransactionDetailsLocators.URL)
            transaction_id = transaction_details.get_transaction_id()
        with allure.step('Proceed to find transaction page.'):
            transaction_details.proceed_to_find_transactions()
        with allure.step('Validation that find transaction page is opened.'):
            find_transaction = FindTransactionPage(driver, FindTransactionLocators.URL)
            find_transaction.find_transaction_page_is_expected()
        with allure.step('Specify transaction id for search.'):
            find_transaction.specify_transaction_id(transaction_id)
        with allure.step('Click search button.'):
            find_transaction.submit_by_transaction_id()
        with allure.step('Validation that transaction was found.'):
            find_transaction.is_successful()
    
    @allure.title("Validation that transaction can't be found by incorrect transaction id number.")
    def test_find_by_incorrect_id(self, driver):
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
        with allure.step('Proceed to find transaction page.'):
            account_overview.proceed_to_find_transactions()
        with allure.step('Validation that find transaction page is opened.'):
            find_transaction = FindTransactionPage(driver, FindTransactionLocators.URL)
            find_transaction.find_transaction_page_is_expected()
        with allure.step('Specify transaction id for search.'):
            find_transaction.specify_transaction_id(random.randint(10000, 100000))
        with allure.step('Click search button.'):
            find_transaction.submit_by_transaction_id()
        with allure.step('Validation that transaction was not found.'):
            find_transaction.is_not_successful()
    
    @allure.title("Validation that transaction can't be found if id field is empty.")
    def test_find_with_empty_id(self, driver):
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
        with allure.step('Proceed to find transaction page.'):
            account_overview.proceed_to_find_transactions()
        with allure.step('Validation that find transaction page is opened.'):
            find_transaction = FindTransactionPage(driver, FindTransactionLocators.URL)
            find_transaction.find_transaction_page_is_expected()
        with allure.step('Click search button.'):
            find_transaction.submit_by_transaction_id()
        with allure.step('Validation that search was not initiated.'):
            assert find_transaction.find_visible_element(FindTransactionLocators.REQUIRED).is_displayed() is True
    
    @allure.title("Validation that user can find transaction by date.")
    def test_find_by_proper_date(self, driver):
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
        with allure.step('Proceed to bill pay.'):
            account_overview.proceed_to_bill_pay()
        with allure.step('Specify all the fields and send payment.'):
            bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
            bill_pay_page.specify_all_the_fields_and_submit()
        with allure.step('Validation that payment is successful.'):
            bill_pay_page.is_successful()
        with allure.step('Proceed to find transaction page.'):
            bill_pay_page.proceed_to_find_transactions()
        with allure.step('Validation that find transaction page is opened.'):
            find_transaction = FindTransactionPage(driver, FindTransactionLocators.URL)
            find_transaction.find_transaction_page_is_expected()
        with allure.step('Specify date.'):
            find_transaction.specify_date()
        with allure.step('Click search button.'):
            find_transaction.submit_by_date()
        with allure.step('Validation that transaction was found by date.'):
            find_transaction.is_successful()
    
    @allure.title("Validation that user can find transaction by proper date range.")
    def test_find_by_correct_date_range(self, driver):
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
        with allure.step('Proceed to bill pay.'):
            account_overview.proceed_to_bill_pay()
        with allure.step('Specify all the fields and submit payment.'):
            bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
            bill_pay_page.specify_all_the_fields_and_submit()
        with allure.step('Validation that payment is successful.'):
            bill_pay_page.is_successful()
        with allure.step('Proceed to find transaction page.'):
            bill_pay_page.proceed_to_find_transactions()
        with allure.step('Validation that find transaction page is opened.'):
            find_transaction = FindTransactionPage(driver, FindTransactionLocators.URL)
            find_transaction.find_transaction_page_is_expected()
        with allure.step('Specify start date.'):
            find_transaction.specify_range_start('04-20-2023')
        with allure.step('Specify end date'):
            find_transaction.specify_range_end(datetime.today().strftime('%m-%d-%Y'))
        with allure.step('Click search button.'):
            find_transaction.submit_by_range()
        with allure.step('Validation that transaction was found by date.'):
            find_transaction.is_successful()
    
    @allure.title("Validation that user can find transaction by amount value.")
    def test_find_by_proper_amount(self, driver):
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
        with allure.step('Proceed to bill pay.'):
            account_overview.proceed_to_bill_pay()
        with allure.step('Specify payee name.'):
            bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
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
            amount = bill_pay_page.specify_amount()
        with allure.step('Click Send button.'):
            bill_pay_page.send_payment()
        with allure.step('Validation that payment is successful.'):
            bill_pay_page.is_successful()
        with allure.step('Proceed to find transaction page.'):
            bill_pay_page.proceed_to_find_transactions()
        with allure.step('Validation that find transaction page is opened.'):
            find_transaction = FindTransactionPage(driver, FindTransactionLocators.URL)
            find_transaction.find_transaction_page_is_expected()
        with allure.step('Specify amount'):
            find_transaction.specify_amount(amount)
        with allure.step('Click search button.'):
            find_transaction.submit_amount()
        with allure.step('Validation that transaction was found by date.'):
            find_transaction.is_successful()
        