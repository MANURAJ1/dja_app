import os
from django.conf import  settings

import pandas as pd
from sqlalchemy import create_engine
dbList=["raj"]
server="DESKTOP-FO3VN7C"

def execute_script(file_name):
    print(os.path.abspath(__file__))
    # print(settings.MEDIA_ROOT+'sql_scripts/table_info.sql')
    print(settings.STATIC_URL + '../sql_scripts/table_info.sql')
    with open(settings.MEDIA_ROOT+r'polls\sql_scripts\table_info.sql')as f:
        sql_query=f.read()
    engine = create_engine('mssql+pymssql://' + server + '/raj')
    a=engine.execute(sql_query)
    data=a.fetchall()
    cols=a.columns()
    df=pd.DataFrame(data=data,columns=cols)
    return df
    # return sql

execute_script("table_info.sql")