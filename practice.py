import pandas as pd
import numpy as np

list1 = ['a','b','c']
list2 = [1,2,3]

res = dict(zip(list1,list2))

df = pd.Dataframe(res)
