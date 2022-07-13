# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:28:54 2022

@author: 黄海军
"""

long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""

# 要求JSON格式输出
outputObject = {};
 
paragraphs = long_text.split('\n');
 
sub_fund = [];
sub_fund_object = {};
isin_list = [];
 
# Key 'name'
name = paragraphs[1];
outputObject["name"] = name;
 
# Key 'lei'
lei  = paragraphs[2];
outputObject["lei"] = lei;
 
# 循环剩下段落
for i in range(3,len(paragraphs)):
    # 检测是否为TITLE行
    if (paragraphs[i].find('.') != -1): 
        # 处理非空的 sub_fund
        if (len(isin_list) != 0):
            sub_fund_object["isin"] = isin_list; 
            sub_fund.append(sub_fund_object);
 
            sub_fund_object = {}; # 残留处理
            isin_list = [];
 
        # 设置字典
        sub_fund_object["title"] = paragraphs[i];
    else: # isin行
        isin_list.append(paragraphs[i]);
 
# 最后一行的sub_fund
if (len(isin_list) != 0):
    sub_fund_object["isin"] = isin_list; 
    sub_fund.append(sub_fund_object); 
 
    sub_fund_object = {}; 
    isin_list = [];
 
# 送进Object
outputObject["sub_fund"] = sub_fund;
 
print(outputObject);