import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pyjavaproperties import Properties


@pytest.fixture(scope="class")
def login_logout(request):
    pfile = Properties()
    try:
        pfile.load(open("../config.properties"))
    except:
        pfile.load(open("config.properties"))
    browser = pfile['browser']
    url = pfile['url']
    use_grid = pfile['use_grid']
    grid_url = pfile['grid_url']
    if use_grid == 'no':
        if browser == 'chrome':
            browser_option = webdriver.ChromeOptions()
            browser_option.add_argument("--disable-notifications")
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=browser_option)
            print('Launched chrome browser in local system')
        else:
            browser_option = webdriver.FirefoxOptions()
            browser_option.add_argument("--disable-notifications")
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=browser_option)
            print('Launched firefox browser in local system')
    else:
        if browser == 'chrome':
            browser_option = webdriver.ChromeOptions()
            print('Launched chrome browser in remote system')
        else:
            browser_option = webdriver.FirefoxOptions()
            print('Launched firefox browser in remote system')
        driver = webdriver.Remote(grid_url, options=browser_option)
    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.close()
