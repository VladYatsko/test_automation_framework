from locators.account_overview_locators import AccountOverviewLocators
from locators.register_locators import RegisterPageLocators
from locators.request_loan_locators import RequestLoanLocators
from pages.account_overview_page import AccountOverviewPage
from pages.register_page import RegisterPage
from pages.request_loan_page import RequestLoanPage


class TestRequestLoan:
    def test_valid_loan_request(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.open_page()
        register_page.register_page_is_expected()
        register_page.full_register()
        account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
        account_overview.open_page()
        account_overview.proceed_to_request_loan()
        request_loan = RequestLoanPage(driver, RequestLoanLocators.URL)
        request_loan.request_loan_page_is_expected()
        request_loan.input_loan_amount(100)
        request_loan.input_down_payment(100)
        request_loan.apply_for_loan()
        request_loan.is_approved()
    
    def test_loan_greater_than_balance(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.open_page()
        register_page.register_page_is_expected()
        register_page.full_register()
        account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
        account_overview.open_page()
        actual_balance = float(account_overview.get_balance())
        account_overview.proceed_to_request_loan()
        request_loan = RequestLoanPage(driver, RequestLoanLocators.URL)
        request_loan.request_loan_page_is_expected()
        request_loan.input_loan_amount(actual_balance + 1)
        request_loan.input_down_payment(actual_balance + 1)
        request_loan.apply_for_loan()
        request_loan.is_declined()
        
    def test_with_missing_argument(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.open_page()
        register_page.register_page_is_expected()
        register_page.full_register()
        account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
        account_overview.open_page()
        account_overview.proceed_to_request_loan()
        request_loan = RequestLoanPage(driver, RequestLoanLocators.URL)
        request_loan.request_loan_page_is_expected()
        request_loan.input_loan_amount(100)
        request_loan.apply_for_loan()
        request_loan.is_blocked()
        
    def test_with_using_text(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.open_page()
        register_page.register_page_is_expected()
        register_page.full_register()
        account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
        account_overview.open_page()
        account_overview.proceed_to_request_loan()
        request_loan = RequestLoanPage(driver, RequestLoanLocators.URL)
        request_loan.request_loan_page_is_expected()
        request_loan.input_loan_amount("asd")
        request_loan.input_down_payment("asd")
        request_loan.apply_for_loan()
        request_loan.is_blocked()
        