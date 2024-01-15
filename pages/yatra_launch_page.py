import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

from generic.base_class import BaseClass
from generic.utilities import Utils
from pages.search_flights_page import SearchFlightsPage


class LaunchPage(BaseClass):
    log = Utils.custom_logger()

    def __init__(self, driver):
        self.driver = driver

    going_from_field = (By.XPATH, "//input[@id='BE_flight_origin_city']")
    going_to_field = (By.XPATH, "//input[@id='BE_flight_arrival_city']")
    search_results_list = (By.XPATH, "//div[@class='viewport']//div[1]/li")
    dept_date_field = (By.XPATH, "//input[@id='BE_flight_origin_date']")
    all_dates_field = (By.XPATH, "//div[@id='monthWrapper']//td[@class!='inActiveTD' and @class!='inActiveTD weekend' and @class!='holiday-desc']")
    search_flights_button = (By.XPATH, "//input[@value='Search Flights']")

    def get_going_from_field(self):
        return self.wait_until_element_is_clickable(*self.going_from_field)

    def get_search_results_list(self):
        return self.wait_until_presence_of_elements(*self.search_results_list)

    def going_from(self, goingfrom):
        self.get_going_from_field().click()
        self.get_going_from_field().send_keys(goingfrom)
        search_results = self.get_search_results_list()
        self.log.info(len(search_results))
        for result in search_results:
            self.log.info(result.text)
            if goingfrom in result.text:
                result.click()
                break
        self.get_going_from_field().send_keys(Keys.ENTER)

    def get_going_to_field(self):
        return self.wait_until_element_is_clickable(*self.going_to_field)

    def going_to(self, goingto):
        self.get_going_to_field().click()
        self.get_going_to_field().send_keys(goingto)
        search_results = self.get_search_results_list()
        self.log.info(len(search_results))
        for result in search_results:
            self.log.info(result.text)
            if goingto in result.text:
                result.click()
                break

    def get_dept_date_field(self):
        return self.wait_until_element_is_clickable(*self.dept_date_field)

    def get_all_dates_list(self):
        return self.wait_until_presence_of_elements(*self.all_dates_field)

    def dept_date(self, deptdate):
        self.get_dept_date_field().click()
        all_dates = self.get_all_dates_list()
        for date in all_dates:
            if date.get_attribute("data-date") == deptdate:
                date.click()
                break

    def click_on_search_btn(self):
        self.driver.find_element(*self.search_flights_button).click()

    def enter_flight_details(self, goingfrom, goingto, deptdate):
        self.going_from(goingfrom)
        self.going_to(goingto)
        self.dept_date(deptdate)
        self.click_on_search_btn()
        search_flights_result = SearchFlightsPage(self.driver)
        return search_flights_result
