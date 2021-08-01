import json
import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'data_2.json')

with open(r'C:/Users/User/Desktop/졸프/2021-graduation-project/data_1.json', 'rt', encoding='utf-8') as data_1:
    data1 = json.load(data_1)

with open(filename, 'rt', encoding='utf-8') as data_2:
    data2 = json.load(data_2)

with open(r'C:/Users/User/Desktop/졸프/2021-graduation-project/data_3.json', 'rt', encoding='utf-8') as data_3:
    data3 = json.load(data_3)

with open(r'C:/Users/User/Desktop/졸프/2021-graduation-project/data_4.json', 'rt', encoding='utf-8') as data_4:
    data4 = json.load(data_4)

with open("CU_Data.json", "w", encoding='utf-8') as CU_Data:
    json.dump(data1+data2+data3+data4, CU_Data,
              ensure_ascii=False, indent='\t')
