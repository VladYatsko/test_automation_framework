from locators.account_overview_locators import AccountOverviewLocators
from locators.bill_pay_locators import BillPayLocators
from locators.register_locators import RegisterPageLocators
from pages.account_overview_page import AccountOverviewPage
from pages.bill_pay_page import BillPayPage
from pages.register_page import RegisterPage


class TestBillPage:
    def test_payment_with_no_arguments(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.open_page()
        register_page.register_page_is_expected()
        register_page.full_register()
        bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
        bill_pay_page.open_page()
        bill_pay_page.send_payment()
        assert len(bill_pay_page.find_visible_elements(BillPayLocators.ERROR_MSG)) == 9
        
    def test_payment_with_missing_argument(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.open_page()
        register_page.register_page_is_expected()
        register_page.full_register()
        bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
        bill_pay_page.open_page()
        bill_pay_page.specify_first_name()
        bill_pay_page.specify_address()
        bill_pay_page.specify_city()
        bill_pay_page.specify_state()
        bill_pay_page.specify_zip_code()
        bill_pay_page.specify_phone_num()
        bill_pay_page.specify_account_and_verify()
        bill_pay_page.send_payment()
        bill_pay_page.is_not_successful()
        
    def test_payment_with_proper_data(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.open_page()
        register_page.register_page_is_expected()
        register_page.full_register()
        bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
        bill_pay_page.open_page()
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
        
    def test_payment_from_another_account(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.open_page()
        register_page.register_page_is_expected()
        register_page.full_register()
        account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
        account_overview.open_page()
        old_balance = float(account_overview.get_balance())
        account_overview.proceed_to_bill_pay()
        bill_pay_page = BillPayPage(driver, BillPayLocators.URL)
        bill_pay_page.open_page()
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
        bill_pay_page.proceed_to_accounts_overview()
        account_overview.account_overview_page_is_expected()
        new_balance = float(account_overview.get_balance())
        assert new_balance == old_balance - float(amount_to_send)
    