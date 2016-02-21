# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 16:16:28 2016

@author: Connor
"""

from os import walk
import pandas as pd


folder = 'C:\Users\lp0ougx3\Desktop\Development\knox_realty\wanted_data'

f = []
for (dirpath, dirnames, filenames) in walk(folder):
    f.extend(filenames)
    break

for fname in f:
    df = pd.read_csv(folder+ '\\' + fname)
    
    df = df[df['RegionName'] == 37917]
    
    df.to_csv(fname, index = False)
    
