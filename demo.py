import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


option=webdriver.ChromeOptions()
option.add_argument("--disable-notifications")
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
# driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.yatra.com")
wait=WebDriverWait(driver,10)
dept_from=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_origin_city']")))
dept_from.click()
dept_from.send_keys("Bangalore")
search_results=wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='viewport']//div[1]/li")))
print(len(search_results))
for result in search_results:
    print(result.text)
    if "Bangalore (BLR)" in result.text:
        result.click()
        break
dept_from.send_keys(Keys.ENTER)
going_to=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_arrival_city']")))
going_to.click()
going_to.send_keys("Mum")
search_results=wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='viewport']//div[1]/li")))
print(len(search_results))
for result in search_results:
    print(result.text)
    if "Mumbai (BOM)" in result.text:
        result.click()
        break
dept_date=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_origin_date']")))
dept_date.click()
all_dates=wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@id='monthWrapper']//td[@class!='inActiveTD']")))
for date in all_dates:
    if date.get_attribute("data-date")=="31/01/2024":
        date.click()
        break
driver.find_element(By.XPATH,"//input[@value='Search Flights']").click()
page_length=driver.execute_script("window.scrollTo(0,document.body.scrollHeight);var page_length=document.body.scrollHeight;return page_length")
match=False
while match==False:
    last_count=page_length
    if last_count==page_length:
        page_length="window.scrollTo(0,document.body.scrollHeight);var page_length=document.body.scrollHeight;return page_length"
        match=True
    time.sleep(2)
driver.find_element(By.XPATH,"//p[text()='1']").click()
all_stops=wait.until(EC.presence_of_all_elements_located((By.XPATH,"//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop(s)') ]")))
print(len(all_stops))
try:
    for stop in all_stops:
        print('The stop is:',stop.text)
        assert stop.text=='1 Stop'
        print('assert pass')
except:
    print('assert fail')
time.sleep(5)
driver.close()


