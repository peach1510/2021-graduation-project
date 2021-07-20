from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome()

# C:\Users\sonso\Downloads\phantomjs-2.1.1-windows\bin

driver.implicitly_wait(3)

driver.get('http://cu.bgfretail.com/product/product.do?category=product&depth2=4&sf=N')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
next = driver.find_element_by_css_selector("#dataTable > div.prodListBtn > div.prodListBtn-w > a")
next.click()
# next.click()
# next.click()
# while True:
#     #do stuff on the page
#     if next:
#         next.click()
#     else:
#         break


elements = driver.find_elements_by_css_selector('#dataTable > div.prodListWrap > ul > li')
print( '상품 개수: {}'.format( len(elements) ) )
for el in elements:
    el_title = el.find_element_by_css_selector('p.prodName > span')
    el_price = el.find_element_by_css_selector('p.prodPrice > span')

    title = el_title.text
    price = el_price.text
    
    print( '='*50 )

    print( 'title: {}'.format( title ) )
    print( 'price: {}'.format( price ) )



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