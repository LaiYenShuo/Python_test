# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 13:33:41 2018

@author: ms022
"""
import numpy as np
import pandas as pd
df = pd.DataFrame({'A' : pd.date_range('20130101',periods=3),'B' : pd.date_range('20160101',periods=3,tz='US/Eastern')})
df = pd.DataFrame(np.random.rand(10,2),columns=['a','b'])               
df.plot.bar(color=['red','blue'])
#10.22.18.97
