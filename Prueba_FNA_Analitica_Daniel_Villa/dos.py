#!/usr/bin/python3
"""Join the three databases in a new table call TABLE"""

#importar modulos necesarios
import pandasql as psql
import pandas as pd

# Crear dataframes con panda de bases de datos .csv
act_ret = pd.read_csv('/home/daniel/Prueba_FNA_Analitica_Daniel_Villa/act_ret.csv', sep=';', decimal=',', encoding = 'utf8', quotechar = "'")
credito_pag = pd.read_csv('/home/daniel/Prueba_FNA_Analitica_Daniel_Villa/credito_pag.csv', sep=';', decimal=',', encoding = 'utf8', quotechar = "'") 
credito_vig = pd.read_csv('/home/daniel/Prueba_FNA_Analitica_Daniel_Villa/credito_vig.csv', sep=';', decimal=',', encoding = 'utf8', quotechar = "'") 

# Union de las 3 bases de datos en una tabla (FINAL)
FINAL =  psql.sqldf("SELECT ENTE FROM act_ret UNION SELECT ENTE FROM credito_vig UNION SELECT ENTE FROM credito_pag")
# Unir columna ESTADO_AFILIADO a FINAL
FINAL  = psql.sqldf("SELECT FINAL.ENTE, act_ret.ESTADO_AFILIADO, act_ret.ESTADO FROM FINAL LEFT JOIN act_ret ON FINAL.ENTE = act_ret.ENTE;")
# Crear y llenar columna IND_ESTADO
FINAL  = psql.sqldf("SELECT ENTE, ESTADO_AFILIADO, CASE WHEN TRIM(ESTADO) = 'ANP' OR TRIM(ESTADO) = 'AAP' THEN 1 ELSE 0 END IND_ESTADO FROM FINAL;")
# Crear y llenar columna IND_CRED_VIG
FINAL  = psql.sqldf("SELECT ENTE, ESTADO_AFILIADO, IND_ESTADO, CASE WHEN ENTE IN (SELECT DISTINCT ENTE FROM credito_vig) THEN 1 ELSE 0 END IND_CRED_VIG FROM FINAL;")
# Crear y llenar columna IND_CRED_PAG
FINAL  = psql.sqldf("SELECT ENTE, ESTADO_AFILIADO, IND_ESTADO, IND_CRED_VIG, CASE WHEN ENTE IN (SELECT DISTINCT ENTE FROM credito_pag) THEN 1 ELSE 0 END IND_CRED_PAG FROM FINAL;")
# Crear dataframe GROUP_BY donde se resuma toda la información anterior
GROUP_BY  = psql.sqldf("SELECT IND_ESTADO,IND_CRED_VIG, IND_CRED_PAG,  COUNT(ENTE) AS ENTES FROM FINAL WHERE ESTADO_AFILIADO = 'ACTIVO' GROUP BY IND_ESTADO, IND_CRED_VIG, IND_CRED_PAG;")

# mostrar primeros registros de FINAL y GROUP_BY
FINAL.head()
GROUP_BY.head()
