from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome()
import time


driver.implicitly_wait(3)
driver.get('http://cu.bgfretail.com/product/product.do?category=product&depth2=4&sf=N')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
#next = driver.find_element_by_css_selector("#dataTable > div.prodListBtn > div.prodListBtn-w > a")
driver.find_element_by_xpath("//*[@id='dataTable']/div[2]/div[1]/a").click()
driver.find_element_by_xpath("//*[@id='dataTable']/div[3]/div[1]/a").click()
driver.find_element_by_xpath("//*[@id='dataTable']/div[4]/div[1]/a").click()
driver.find_element_by_xpath("//*[@id='dataTable']/div[5]/div[1]/a").click()
driver.find_element_by_xpath("//*[@id='dataTable']/div[6]/div[1]/a").click()
driver.find_element_by_xpath("//*[@id='dataTable']/div[7]/div[1]/a").click()

def print_product(elements):
    print( '상품 개수: {}'.format( len(elements) ) )
    for el in elements:
        el_title = el.find_element_by_css_selector('p.prodName > span')
        el_price = el.find_element_by_css_selector('p.prodPrice > span')

        title = el_title.text
        price = el_price.text
    
        print( '='*50 )

        print( 'title: {}'.format( title ) )
        print( 'price: {}'.format( price ) )



print_product(driver.find_elements_by_xpath("//*[@id='dataTable']/div[1]/ul/li[*]"))
print_product(driver.find_elements_by_xpath("//*[@id='dataTable']/div[2]/ul/li[*]"))
print_product(driver.find_elements_by_xpath("//*[@id='dataTable']/div[3]/ul/li[*]"))
print_product(driver.find_elements_by_xpath("//*[@id='dataTable']/div[4]/ul/li[*]"))
print_product(driver.find_elements_by_xpath("//*[@id='dataTable']/div[5]/ul/li[*]"))
print_product(driver.find_elements_by_xpath("//*[@id='dataTable']/div[6]/ul/li[*]"))
print_product(driver.find_elements_by_xpath("//*[@id='dataTable']/div[7]/ul/li[*]"))


    


# print( elements[0].get_attribute('innerHTML') )




# my_titles = soup.select(
#     'h3 > a'
#     )
# ## my_titles는 list 객체
# for title in my_titles:
#     ## Tag안의 텍스트
#     print(title.text)
#     ## Tag의 속성을 가져오기(ex: href속성)
#     print(title.get('href'))

#dataTable > div.prodListBtn > div.prodListBtn-w > a
#dataTable > div:nth-child(34)