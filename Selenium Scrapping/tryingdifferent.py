from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from csv import writer
url = 'https://www.betfair.com/exchange/plus/horse-racing/market/1.206263786?nodeId=31895867.0657'
driver=webdriver.Chrome()
driver.get(url)
print(driver.title)
try:
    time.sleep(15)
    link = driver.find_element(By.CLASS_NAME, 'TODAYS_CARD')
    link.click()
    time.sleep(15)
    runnerLines=driver.find_elements(By.CLASS_NAME,'runner-line')
    lstOfRunner=[]
    with open('data.csv', 'w', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header = ['1st column', '2nd column', '2nd column', '3rd column','3rd column','4th column','4th column','5th column','5th column','6th column','6th column','7th column','7th column','8th column','8th column']
        thewriter.writerow(header)
        for runnerLine in runnerLines:
            lstOfRunner.append(runnerLine.text)
        for runner in lstOfRunner:
            data = runner.split("\n")
            thewriter.writerow(data)
    # print(driver.find_element(By.CLASS_NAME,'main-mv-runners-list-wrapper').text)
    print(lstOfRunner)
finally:
    driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()