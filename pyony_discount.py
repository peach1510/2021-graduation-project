from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

import requests
from bs4 import BeautifulSoup
import json
from collections import OrderedDict  # 파이썬 dict는 자동정렬이라 그렇지 않은 ordereddict사용


#####################################################################

# crawler함수는 brand이름과(cu,seven,gs25,ministop,emart24 중하나)
# category(생활용품,음료,아이스크림.....중하나)
# event(1+1,2+1,3+1) 을 <<<입력>>> 받아
# <<<출력>>>으로 해당 입력에 맞는 품목을 json파일로 생성해주는 함수이다.

# 입력시에 아무것도 입력하지 않으면 필터링 되지 않은 모든 데이터가 json으로 나오게 된다.
# 예를들면, 1+1을 입력하지 않으면, 1+1/2+1/3+1 모든 항목이 포함돼 나온다.
# 마찬가지로, category를 입력하지 않으면, 생활용품/음료/아이스크림 등 모든 품목에 대한 정보가 포함된다.

#####################################################################


def crawler(brand_name, category, event):
    if event == '1':
        event = '1+1'
    elif event == '2':
        event = '2+1'
    elif event == '3':
        event = '3+1'
    elif event == '4':
        event = '4+1'
    else:
        event = None

    if brand_name == 'cu':
        brand_name = 'cu'
    elif brand_name == 'gs':
        brand_name = 'gs25'
    elif brand_name == 'seven':
        brand_name = 'seven'
    elif brand_name == 'mini':
        brand_name = 'ministop'
    elif brand_name == 'emart':
        brand_name = 'emart24'
    else:
        brand_name = None

    if category == 'beverage':
        category = '음료'
    elif category == 'snack':
        category = '과자류'
    elif category == 'food':
        category = '식품'
    elif category == 'ice':
        category = '아이스크림'
    elif category == 'goods':
        category = '생활용품'
    else:
        category = None

    print(brand_name, category, event)

    Data = []
    page = "1"

    body_data = ['0']*32

    while True:
        flag, flag2 = 0, 0

        if len(body_data) < 32:
            break

        if brand_name:
            res = requests.get('https://pyony.com/brands/' +
                               brand_name + '/?page=' + page)
        else:
            res = requests.get('https://pyony.com/search/?page=' + page)
            flag = 1

        if not category:
            flag2 = 1

        soup = BeautifulSoup(res.content, 'html.parser')
        body = soup.find('body')
        body_data = body.findAll('a', class_='deco-none')

        page = str(int(page) + 1)

        for data in body_data:

            # 행사품목 페이지당 리스트 32개씩나옴 예외처리해야함 실제 data는 <= 32
            try:
                name = data.find('strong').get_text()
                Category = data.find(
                    'small', class_='float-right font-weight-bold').get_text()
                total_price = data.get_text().split(
                    '\n')[13][:-1].strip().replace(',', '')

                if brand_name:
                    how_many = data.find(
                        'span', class_='badge bg-' + brand_name + ' text-white').get_text()
                else:
                    how_many = data.findAll('span')[1].get_text()
                    brand_name = data.findAll('small')[0].get_text()

                img_url = data.find('img').attrs['src']
                informations = OrderedDict()

                informations['BrandName'] = brand_name

                informations['ProductName'] = name

                informations['CategoryName'] = Category
                informations['Price'] = total_price
                informations['EventName'] = how_many
                informations['ImageURL'] = img_url

                if flag == 1:
                    brand_name = None

                if event and category:
                    if flag2 == 1:
                        Category = None
                    if event == how_many and category == Category:
                        Data.append(informations)
                    else:
                        continue

                elif event and not category:
                    if flag2 == 1:
                        Category = None
                    if event == how_many:
                        Data.append(informations)
                    else:
                        continue

                elif not event and category:
                    if flag2 == 1:
                        Category = None
                    if category == Category:
                        Data.append(informations)

                    else:
                        continue
                else:
                    if flag2 == 1:
                        Category = None
                    Data.append(informations)

            except:
                break
    #print(json.dumps(Data,ensure_ascii = False, indent='\t'))
    with open('data.json', 'w', encoding='utf-8') as make_file:
        json.dump(Data, make_file, ensure_ascii=False, indent='\t')

    return json.dumps(Data, ensure_ascii=False, indent='')


def index(request):
    brand_name = request.GET['brand']
    category = request.GET['category']
    event = request.GET['event']
    returndata = crawler(brand_name, category, event)
    return HttpResponse(returndata)


crawler('', '', '1')
