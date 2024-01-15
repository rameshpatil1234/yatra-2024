import pytest
import softest
from pages.yatra_launch_page import LaunchPage
from generic.utilities import Utils
from ddt import ddt, unpack, data


@pytest.mark.usefixtures("login_logout")
@ddt
class TestSearchFlights(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    @data(*Utils.read_data_from_excel("data/input.xlsx", "yatra-lp"))
    @unpack
    def test_search_flights(self, goingfrom, goingto, date, stop):
        search_flights_results = self.lp.enter_flight_details(goingfrom, goingto, date)
        self.lp.page_scroll()
        search_flights_results.filter_flights_by_stop(stop)
        all_stops = search_flights_results.get_all_stops_list()
        print(len(all_stops))
        self.ut.assert_list_item_text(all_stops, stop)
