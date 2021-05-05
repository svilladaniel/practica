#!/usr/bin/python3
"""Visualization"""

#importación de modulos necesarios
import pandasql as psql
import pandas as pd
import matplotlib.pyplot as plt

# Abrir la base de datos .csv con panda y guradarla en variable visual
visual = pd.read_csv('/home/daniel/Prueba_FNA_Analitica_Daniel_Villa/Prueba_FNA_Analitica_DATOS.csv', sep='|', decimal=',', encoding = 'ISO-8859-1', quotechar = "'")
# añadir columna utilidad
visual  = psql.sqldf("SELECT FIN_FLO_INGRESOS_MENSUALES, FIN_FLO_EGRESOS_MENSUAL, CLI_DTM_FEC_NACIMIENTO, CLI_STR_DEPTO_DOMICILIO, CLI_STR_DESC_ACT_ECONOMICA, CLI_STR_NOM_RAZON_SOCIAL_EMP, (FIN_FLO_INGRESOS_MENSUALES - FIN_FLO_EGRESOS_MENSUAL) AS UTILIDAD FROM visual;")
#organizar dataframe con estadisticas generales
estad = visual.describe()
# organizar dataframe que muestre top 10 de actividades económicas con mayor utilidad y que las organice de mayor a menor
util = visual[['CLI_STR_DESC_ACT_ECONOMICA','UTILIDAD']].sort_values(by="UTILIDAD",ascending=False).head(10)
# mostrar dataframes
visual.head()
estad
util
# mostrar grafica de actividad económica vs utilidad
util.plot('CLI_STR_DESC_ACT_ECONOMICA', kind = 'bar')


