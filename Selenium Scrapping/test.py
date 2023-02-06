from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import sys
from selenium.webdriver.chrome.service import Service
url = 'https://www.betfair.com/exchange/plus/horse-racing/market/1.206263786?nodeId=31895867.0657'
driver=webdriver.Chrome()
driver.get(url)
print(driver.title)
try:
    lst=driver.find_elements(By.CLASS_NAME,"runner-line")
    for runner in lst:
        h1 = runner.find_element(By.XPATH, './/*[@id="main-wrapper"]/div/div[2]/div/ui-view/div/div/div[1]/div[3]/div/div[1]/div/bf-main-market/bf-main-marketview/div/div[2]/bf-marketview-runners-list[2]/div/div/div/table/tbody/tr[1]/td/div[2]/div[2]/bf-runner-info/div/div/div[3]/h3').text
        print(h1)
except:
    print("not find")


# chrome_driver_path = Service("E:\PycharmProjects\Selenium Scrapping\chromedriver.exe")
#
# chrome_options = Options()
# chrome_options.add_argument('--headless')
#
# webdriver = webdriver.Chrome(service=chrome_driver_path, options=chrome_options)
#
# with webdriver as driver:
#     wait = WebDriverWait(driver, 10)
#     driver.get(url)
#
#     # print(driver.page_source)
#     wait.until(presence_of_element_located((By.CLASS_NAME, 'scrollable-panes-height-taker')))
#     print(driver.title)
#     try:
#         lst=driver.find_elements(By.CLASS_NAME,"runner-line")
#         for runner in lst:
#             h1 = runner.find_element(By.XPATH, './/*[@id="main-wrapper"]/div/div[2]/div/ui-view/div/div/div[1]/div[3]/div/div[1]/div/bf-main-market/bf-main-marketview/div/div[2]/bf-marketview-runners-list[2]/div/div/div/table/tbody/tr[1]/td/div[2]/div[2]/bf-runner-info/div/div/div[3]/h3').text
#             print(h1)
#     except:
#         print("not find")
#     # results = driver.find_element(By.CLASS_NAME, "mv-runner-list-container")
#     # for quote in results:
#     #     quoteArr = quote.text.split('\n')
#     #     print(quoteArr)
#     #     print()
#
#         # must close the driver after task finished
#     driver.close()
#
