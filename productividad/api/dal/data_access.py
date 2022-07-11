from unittest import result
from django.db import connection
import json
import pandas as pd

class DataAcess():


    def Excute(query,params):

        Resultquery = pd.read_sql_query(query,connection,params=params)
        filas = Resultquery.loc[0,"filas_afectadas"]

        if filas>0:
         return True
        else:
         return False

    def QuerySingle(query,params):
            resultQuery = json.loads(pd.read_sql_query(query,connection,params=params).to_json(orient="records"))
            
            if resultQuery:
                return resultQuery[0]
            else:
                return None

    def Query(query,params):
            resultQuery = json.loads(pd.read_sql_query(query,connection,params=params).to_json(orient="records"))
            return resultQuery


    def QueryNoParams(query):
            resultQuery = json.loads(pd.read_sql(query, connection).to_json(orient="records"))
        
            return resultQuery


    def QueryPandas(query,params):
        resultQuery = pd.read_sql(query, connection,params=params)

        return resultQuery

    def QueryPandasNoParams(query):
        resultQuery = pd.read_sql(query, connection)
        
        return resultQuery


    
