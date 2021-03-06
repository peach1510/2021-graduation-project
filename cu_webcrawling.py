from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import json
from collections import OrderedDict
import time

driver = webdriver.Chrome(
    executable_path=r'C:\Users\User\Downloads\chromedriver')

driver.implicitly_wait(3)

driver.get(
    'http://cu.bgfretail.com/product/product.do?category=product&depth2=4&sf=N')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

'''
while True:
    try:
        next = driver.find_element_by_css_selector("#dataTable > div.prodListBtn > div.prodListBtn-w > a")
        next.click()
        time.sleep(1)
    except:
        break

'''

file_data = OrderedDict()
datas = []

i = 1
childPoint = 17

while True:
    try:

        page = "#dataTable > div:nth-child(" + str(childPoint) + ")"

        if i > 40:
            i = 1
            childPoint += 17
            next = driver.find_element_by_css_selector(
                "#dataTable > div.prodListBtn > div.prodListBtn-w > a")
            next.click()

        info = driver.find_element_by_css_selector(
            page + " > ul > li:nth-child(" + str(i) + ")")
        info.click()

        elements = driver.find_elements_by_css_selector(
            '#gnb > div > div.prodDetailWrap > div.prodDetail > div.prodDetail-e')

        for el in elements:
            el_title = el.find_element_by_css_selector('p')
            el_price = el.find_element_by_css_selector(
                'div > dl:nth-child(1) > dd > p > span')
            el_info = el.find_element_by_css_selector(
                'div > dl:nth-child(2) > dd > ul > li')
            el_tag = el.find_element_by_css_selector(
                'div > dl:nth-child(3) > dd > ul > li')

            title = el_title.text
            price = el_price.text
            info = el_info.text
            tag = el_tag.text

            # print('='*50)

        #    print('title: {}'.format(title))
        #    print('price: {}'.format(price))
        #    print('info: {}'.format(info))
        #    print('tag: {}'.format(tag))
        #file_data["title"] = title
        #file_data["price"] = price
        #file_data["info"] = info
        #file_data["tag"] = tag

        datas.append({"title": title, "price": price,
                     "info": info, "tag": tag})

        #print(json.dumps(file_data, ensure_ascii=False, indent="\t"))

        with open('data_1.json', 'w', encoding='utf-8') as make_file:
            json.dump(datas, make_file, ensure_ascii=False, indent='\t')

        i += 1
        driver.back()

    except NoSuchElementException:
        next = driver.find_element_by_css_selector(
            "#dataTable > div.prodListBtn > div.prodListBtn-w > a")
        next.click()

    except Exception as ex:
        print(ex)
