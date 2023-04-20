from locators.account_activity_locators import AccountActivityLocators
from locators.account_overview_locators import AccountOverviewLocators
from locators.open_account_locators import OpenAccountLocators
from locators.register_locators import RegisterPageLocators
from locators.transfer_funds_locators import TransferFundsLocators
from pages.account_activity_page import AccountActivityPage
from pages.account_overview_page import AccountOverviewPage
from pages.open_account_page import OpenAccountPage
from pages.register_page import RegisterPage
from pages.transfer_funds_page import TransferFundsPage


class TestTransferFunds:
    def test_with_no_amount(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.open_page()
        register_page.register_page_is_expected()
        register_page.full_register()
        open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
        open_account.open_page()
        open_account.open_account_page_is_expected()
        open_account.proceed_to_transfer_funds()
        transfer_funds = TransferFundsPage(driver, TransferFundsLocators.URL)
        transfer_funds.transfer_funds_page_is_expected()
        transfer_funds.move_to_element_and_submit(TransferFundsLocators.TRANSFER_BUTTON)
        transfer_funds.is_not_successful()
        
    def test_with_valid_amount(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.open_page()
        register_page.register_page_is_expected()
        register_page.full_register()
        open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
        open_account.open_page()
        open_account.open_account_page_is_expected()
        open_account.proceed_to_accounts_overview()
        account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
        account_overview.account_overview_page_is_expected()
        account_overview.proceed_to_transfer_funds()
        transfer_funds = TransferFundsPage(driver, TransferFundsLocators.URL)
        transfer_funds.transfer_funds_page_is_expected()
        transfer_funds.specify_amount(100)
        transfer_funds.move_to_element_and_submit(TransferFundsLocators.TRANSFER_BUTTON)
        transfer_funds.is_successful()
        transfer_funds.proceed_to_accounts_overview()
        account_overview.account_overview_page_is_expected()
        account_overview.get_into_account()
        account_activity = AccountActivityPage(driver, AccountActivityLocators.URL)
        account_activity.search_for_activity()
        assert len(account_activity.find_visible_elements(AccountActivityLocators.TRANSACTION_ID)) == 2
        
    def test_with_invalid_amount(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.open_page()
        register_page.register_page_is_expected()
        register_page.full_register()
        open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
        open_account.open_page()
        open_account.open_account_page_is_expected()
        open_account.proceed_to_accounts_overview()
        account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
        account_overview.account_overview_page_is_expected()
        current_balance = float(account_overview.get_balance())
        account_overview.proceed_to_transfer_funds()
        transfer_funds = TransferFundsPage(driver, TransferFundsLocators.URL)
        transfer_funds.transfer_funds_page_is_expected()
        transfer_funds.specify_amount(current_balance + 1)
        transfer_funds.move_to_element_and_submit(TransferFundsLocators.TRANSFER_BUTTON)
        transfer_funds.is_not_successful()
        
    def test_to_another_account_valid_amount(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.open_page()
        register_page.register_page_is_expected()
        register_page.full_register()
        open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
        open_account.open_page()
        open_account.open_account_page_is_expected()
        open_account.select_checking()
        open_account.submit_creation()
        assert open_account.get_new_account_id().is_displayed() is True
        open_account.proceed_to_accounts_overview()
        account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
        account_overview.account_overview_page_is_expected()
        first_acc_balance = float(account_overview.get_balance_by_index(0))
        second_acc_balance = float(account_overview.get_balance_by_index(1))
        account_overview.proceed_to_transfer_funds()
        transfer_funds = TransferFundsPage(driver, TransferFundsLocators.URL)
        transfer_funds.specify_amount(100)
        transfer_funds.select_from_account(0)
        transfer_funds.select_to_account(1)
        transfer_funds.move_to_element_and_submit(TransferFundsLocators.TRANSFER_BUTTON)
        transfer_funds.is_successful()
        transfer_funds.proceed_to_accounts_overview()
        account_overview.account_overview_page_is_expected()
        current_first_balance = float(account_overview.get_balance_by_index(0))
        current_second_balance = float(account_overview.get_balance_by_index(1))
        assert current_first_balance == first_acc_balance - 100
        assert current_second_balance == second_acc_balance + 100
    
    def test_to_another_account_invalid_amount(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.open_page()
        register_page.register_page_is_expected()
        register_page.full_register()
        open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
        open_account.open_page()
        open_account.open_account_page_is_expected()
        open_account.select_checking()
        open_account.submit_creation()
        assert open_account.get_new_account_id().is_displayed() is True
        open_account.proceed_to_accounts_overview()
        account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
        account_overview.account_overview_page_is_expected()
        first_acc_balance = float(account_overview.get_balance_by_index(0))
        account_overview.proceed_to_transfer_funds()
        transfer_funds = TransferFundsPage(driver, TransferFundsLocators.URL)
        transfer_funds.specify_amount(first_acc_balance + 1)
        transfer_funds.select_from_account(0)
        transfer_funds.select_to_account(1)
        transfer_funds.move_to_element_and_submit(TransferFundsLocators.TRANSFER_BUTTON)
        transfer_funds.is_not_successful()
        