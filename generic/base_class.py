import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass:
    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        page_length = self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight);var page_length=document.body.scrollHeight;return page_length")
        match = False
        while match == False:
            last_count = page_length
            if last_count == page_length:
                page_length = "window.scrollTo(0,document.body.scrollHeight);var page_length=document.body.scrollHeight;return page_length"
                match = True
            time.sleep(2)

    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10,2,ignored_exceptions='ElementClickInterceptedException')
        return wait.until(EC.element_to_be_clickable((locator_type, locator)))

    def wait_until_presence_of_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10,2,ignored_exceptions='ElementClickInterceptedException')
        return wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
