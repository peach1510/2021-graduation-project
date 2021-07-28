
# Crawler For CU

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

driver = webdriver.Chrome(
    executable_path=r'C:\Users\User\Downloads\chromedriver')
driver.get('http://cu.bgfretail.com/event/plus.do?category=event&depth2=1&sf=N')

i = 1

while True:

    print("Click : %d" % i)
    i += 1

    driver.execute_script('javascript:nextPage(1)')
    driver.implicitly_wait(3)

    finished = True

    try:
        driver.find_element_by_id('nothing')
    except NoSuchElementException:
        finished = False

    if finished:
        break

html = driver.page_source

print(html)

print("Complete")
