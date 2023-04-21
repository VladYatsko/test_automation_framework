from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, timeout=10)
    
    def open_page(self) -> None:
        self.driver.get(self.url)
    
    def get_title(self) -> str:
        return self.driver.title
    
    def get_url(self) -> str:
        return self.driver.current_url
    
    def find_visible_element(self, locator: tuple) -> WebElement:
        try:
            return self.wait.until(ec.visibility_of_element_located(locator))
        except ValueError:
            return self.wait.until(ec.visibility_of_element_located(locator))
    
    def find_visible_elements(self, locator: tuple) -> list:
        try:
            return self.wait.until(ec.visibility_of_all_elements_located(locator))
        except ValueError:
            return self.wait.until(ec.visibility_of_element_located(locator))
    
    def get_text(self, locator: tuple) -> str:
        return self.wait.until(ec.presence_of_element_located(locator)).text
    
    def send_text(self, locator: tuple, value: str):
        self.wait.until(ec.element_to_be_clickable(locator)).send_keys(value)
    
    def click_element(self, locator: tuple) -> None:
        return self.wait.until(ec.element_to_be_clickable(locator)).click()
    
    def remove_text(self, locator: tuple) -> None:
        return self.wait.until(ec.element_to_be_clickable(locator)).clear()
    
    def complete_alert(self, login: str, password: str) -> None:
        alert_unit = self.driver.switch_to.alert
        alert_unit.send_keys(login)
        action = ActionChains(self.driver)
        action.key_down(Keys.TAB).perform()
        action.key_up(Keys.TAB).perform()
        alert_unit.send_keys(password)
        alert_unit.accept()
        self.driver.switch_to.default_context()
        
    def shift_from_element(self):
        action = ActionChains(self.driver)
        action.key_down(Keys.TAB).perform()
        action.key_up(Keys.TAB).perform()
        
    def submit_by_keyboard(self):
        action = ActionChains(self.driver)
        action.key_down(Keys.ENTER).perform()
        action.key_up(Keys.ENTER).perform()
        
    def move_to_element_and_submit(self, locator):
        action = ActionChains(self.driver)
        action.move_to_element(self.find_visible_element(locator)).click().perform()
    
    def refresh_page(self) -> None:
        return self.driver.refresh()
    
    def return_back(self) -> None:
        return self.driver.back()
    
    def move_forward(self) -> None:
        return self.driver.forward()
