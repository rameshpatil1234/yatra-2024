from selenium.webdriver.common.by import By

from generic.base_class import BaseClass
from generic.utilities import Utils


class SearchFlightsPage(BaseClass):
    log = Utils.custom_logger()
    def __init__(self, driver):
        self.driver = driver

    filter_flight_by_1_stop = (By.XPATH, "//p[text()='1']")
    filter_flight_by_2_stops = (By.XPATH, "//p[text()='2']")
    filter_flight_by_non_stop = (By.XPATH, "//p[text()='0']")
    all_stops_list = (
        By.XPATH, "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop(s)') ]")

    def filter_flights_by_1_stop(self):
        return self.driver.find_element(*self.filter_flight_by_1_stop)

    def filter_flights_by_2_stop(self):
        return self.driver.find_element(*self.filter_flight_by_2_stops)

    def filter_flights_by_non_stop(self):
        return self.driver.find_element(*self.filter_flight_by_non_stop)

    def get_all_stops_list(self):
        return self.wait_until_presence_of_elements(*self.all_stops_list)

    def filter_flights_by_stop(self, bystop):
        if bystop == '1 Stop':
            self.filter_flights_by_1_stop().click()
            self.log.info('Selected flights with 1 stop')
        elif bystop == '2 Stop(s)':
            self.filter_flights_by_2_stop().click()
            self.log.info('Selected flights with 2 stops')
        elif bystop == 'Non Stop':
            self.filter_flights_by_non_stop().click()
            self.log.info('Selected flights with non stop')
        else:
            self.log.info('Please provide valid filter option')

