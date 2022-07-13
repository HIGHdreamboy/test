import requests
import re
import json
import csv
import pandas as pd

headers={

        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'

        }

url='https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner'

response=requests.get(url=url,headers=headers)

#将数据储存到html
with open('origin.html','wb') as f:
    f.write(response.content) 

data_html=response.text

json_str=re.findall('"component":\[(.*)\],',data_html)[0]

json_dict=json.loads(json_str)

caseList=json_dict['caseList']

for case in caseList:

    area=case['area']#地区

    confirmed=case['confirmed']#累计

    curConfirm=case['curConfirm']#现有

    asymptomatic=case['asymptomatic']#新增

    crued=case['crued']#治愈

    died=case['died']#死亡

    
#写入表格   

    with open('./data.csv',mode='a',encoding='utf-8',newline='')as f:

        csv_writer=csv.writer(f)

        csv_writer.writerow([area,asymptomatic,curConfirm,confirmed,crued,died])