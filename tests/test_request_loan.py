import allure
from locators.account_overview_locators import AccountOverviewLocators
from locators.register_locators import RegisterPageLocators
from locators.request_loan_locators import RequestLoanLocators
from pages.account_overview_page import AccountOverviewPage
from pages.register_page import RegisterPage
from pages.request_loan_page import RequestLoanPage


class TestRequestLoan:
    @allure.title("Validation that user is able to request loan in range of amounts matching current balance.")
    def test_valid_loan_request(self, driver):
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
        with allure.step('Proceed to request loan page.'):
            account_overview.proceed_to_request_loan()
        with allure.step('Validation that request loan page is opened.'):
            request_loan = RequestLoanPage(driver, RequestLoanLocators.URL)
            request_loan.request_loan_page_is_expected()
        with allure.step('Specify loan amount with amount in range of balance.'):
            request_loan.input_loan_amount(100)
        with allure.step('Specify down payment with amount in range of balance.'):
            request_loan.input_down_payment(100)
        with allure.step('Click apply for loan button.'):
            request_loan.apply_for_loan()
        with allure.step('Validation that loan request is successful.'):
            request_loan.is_approved()
    
    @allure.title("Validation that request with loan amount > actual balance will be declined.")
    def test_loan_greater_than_balance(self, driver):
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
        actual_balance = float(account_overview.get_balance())
        with allure.step('Proceed to request loan page.'):
            account_overview.proceed_to_request_loan()
        with allure.step('Validation that request loan page is opened.'):
            request_loan = RequestLoanPage(driver, RequestLoanLocators.URL)
            request_loan.request_loan_page_is_expected()
        with allure.step('Specify loan amount with amount: balance + 1.'):
            request_loan.input_loan_amount(actual_balance + 1)
        with allure.step('Specify down payment with amount: balance + 1.'):
            request_loan.input_down_payment(actual_balance + 1)
        with allure.step('Click apply for loan button.'):
            request_loan.apply_for_loan()
        with allure.step('Validation that loan request is declined.'):
            request_loan.is_declined()
    
    @allure.title("Validation that loan can't be requested with missing argument.")
    def test_with_missing_argument(self, driver):
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
        with allure.step('Proceed to request loan page.'):
            account_overview.proceed_to_request_loan()
        with allure.step('Validation that request loan page is opened.'):
            request_loan = RequestLoanPage(driver, RequestLoanLocators.URL)
            request_loan.request_loan_page_is_expected()
        with allure.step('Specify loan amount with amount in range of balance.'):
            request_loan.input_loan_amount(100)
        with allure.step('Click apply for loan button.'):
            request_loan.apply_for_loan()
        with allure.step('Validation that loan was not requested.'):
            request_loan.is_blocked()
    
    @allure.title("Validation that loan can't be requested if text is used for amount fields.")
    def test_with_using_text(self, driver):
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
        with allure.step('Proceed to request loan page.'):
            account_overview.proceed_to_request_loan()
        with allure.step('Validation that request loan page is opened.'):
            request_loan = RequestLoanPage(driver, RequestLoanLocators.URL)
            request_loan.request_loan_page_is_expected()
        with allure.step('Specify any text as loan amount.'):
            request_loan.input_loan_amount("asd")
        with allure.step('Specify any text as down payment.'):
            request_loan.input_down_payment("asd")
        with allure.step('Click apply for loan button.'):
            request_loan.apply_for_loan()
        with allure.step('Validation that loan was not requested.'):
            request_loan.is_blocked()
        