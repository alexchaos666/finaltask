# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 20:30:47 2021

@author: ilin_av
"""

import sqlalchemy as adb
from sqlalchemy import MetaData
import cx_Oracle as ora
import pandas as pd


l_user = 'ilin_av' 
l_pass = 'Deathstar1986'
l_tns = ora.makedsn('13.95.167.129', 1521, service_name = 'pdb1')

l_conn_ora = adb.create_engine(r'oracle://{p_user}:{p_pass}@{p_tns}'.format
        (
        p_user = l_user,
        p_pass = l_pass,
        p_tns = l_tns)
        )

print (l_conn_ora)

l_meta = MetaData (l_conn_ora)
l_meta.reflect()

l_dash_1 = l_meta.tables ['dash_1']
l_dash_2 = l_meta.tables ['dash_2']
l_dash_3 = l_meta.tables ['dash_3']

l_file_excel = pd.read_excel (r'C:\Users\evgen\Downloads\источник данных\dataset.xlsx', sheet_name = 'Лист1')

l_list = l_file_excel.values.tolist()

#Вставка данных в таблицу dash_1

for i in l_list:
    l_dash_1.insert([l_dash_1.c.clients, l_dash_1.c.tb]).values(
        clients = i[0]
        , tb = i[4]
        ).execute()
    print(1)
    
#Вставка данных в таблицу dash_2

for i in l_list:
    l_dash_2.insert([l_dash_2.c.clients, l_dash_2.c.segm]).values(
        clients = i[0]
        , segm = i[3]
        ).execute()
    print(1)
    
#Вставка данных в таблицу dash_3
    
for i in l_list:
    l_dash_3.insert([l_dash_3.c.clients, l_dash_3.c.summ, l_dash_3.c.commission, l_dash_3.c.tb]).values(
        clients = i[0]
        , summ = i[1]
        , commission = i[2]
        , tb = i[4]
        ).execute()
    print(1)
    
    
print ('Обновление')


l_conn_ora.execute (adb.text('BEGIN pkg_ilin.make_rating_dash_final; END;'))

print('Обновлено успешно')   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    