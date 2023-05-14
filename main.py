import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import math

from scipy.optimize import curve_fit, differential_evolution
from scipy.optimize import least_squares, leastsq
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARMA
import quantlib as ql

from datetime import timedelta
import holidays

import pymysql
#import dataReader as reader

# data reader #
conn = pymysql.connect(host = 'containers-us-west-122.railway.app',
                       db='railway',
                       port = 7409,
                       user = 'root',
                       password = 'NrzA30qfm3mYIKoQwna8')


sql_str_db = "select * from yskficc."
sql_str_tbname = "market_credit_matrix"
sql_str_tbname_sw = "market_swap"

sql_str_df = sql_str_db+sql_str_tbname
sql_str_sw = sql_str_db + sql_str_tbname_sw

df_raw = pd.read_sql_query(sql_str_df, conn)
df_sw = pd.read_sql_query(sql_str_sw, conn)

df_sw






