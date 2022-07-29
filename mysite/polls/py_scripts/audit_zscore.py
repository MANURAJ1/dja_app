import os

import pandas as pd
from sqlalchemy import create_engine
dbList=["raj"]
server="DESKTOP-FO3VN7C"

def execute_script(file_name):
    print(os.path.join('..','sql_scripts',file_name))
    print(os.path.abspath(__file__))
    print()

    # with open("../sql_scripts/"+file_name) as f:
    #     sql_query=f.readlines()
    # engine = create_engine('mssql+pymssql://' + server + '/master')
    # return pd.read_sql(sql_query,con=engine)
    return 0

execute_script("table_info.sql")