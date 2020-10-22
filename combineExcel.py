import os
import pandas as pd
import numpy as np

path = os.getcwd()
valid_files = [".xls", ".xlsx"]
df = pd.DataFrame()

for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_files:
        continue
    print("Read file...", f)
    fileExcel = pd.read_excel(os.path.join(path,f), header = None, sheet_name = None)
    for sheet in fileExcel.keys():
    	df = pd.concat([df, fileExcel[sheet]], ignore_index = True)
    print(df.shape)