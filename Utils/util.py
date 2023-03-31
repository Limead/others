import os, sys
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import re
import pandas as pd
import numpy as np
from tqdm import tqdm
import json
import ast


## SQL의 SAFT_CAST 기능 구현
def try_lambda_str(x):
    try:
        if pd.notnull(x):
            x = str(x).replace(',','')
        return float(x)
    except:
        return 0
      
## 문자열 dictionary 객체 변경 기능
def dict_trans(x):
    try:
        return ast.literal_eval(x)
    except:
        return x
      
## 숨김 파일을 제외하고 폴더 내부의 항목 검색 기능
def list_dir(PATH):
    return [f for f in os.listdir(PATH) if not f.startswith('.')]  
  
  
## 문자열 중 날짜 데이터 파싱 기능
def check_date(x):
    x = re.sub('[^A-Za-z0-9가-하]','',str(x))
    try:
        return datetime.strptime(re.search(r'\d{4}\d{2}\d{2}',str(x)).group(), '%Y%m%d').date()
        
    except:
        return x
