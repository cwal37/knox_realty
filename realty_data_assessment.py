# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 16:45:05 2016

@author: Connor
"""
import os
import pandas as pd
from file_walk_with_me import *


# location of unscrubbed (for knoxville) realty data, hundreds of MB, so excluded
# from the repo, you can find th files from zillow on their data page
source_directory = 'C:\Users\lp0ougx3\Desktop\Development\knox_realty\wanted_data'
output_directory = 'C:\Users\lp0ougx3\Desktop\Development\knox_realty\\filtered_data'

# run filter walk when you need to generate new filtered files, otherwise it's
# just an overhead on the whole script running

#filter_walk(source_directory, output_directory, 'RegionName', 37917)

file_names = file_walk(output_directory)
    
# generate dataframes for all files from the filtered files, then some graphing    
for fname in file_names:
    df = pd.read_csv(output_directory + '\\' + fname)
    if len(df.columns)



# not doing this, because I was just creating lsts of strings, I think I can do it
# all in the initial loop of df creation, consolidate it all, and I also don't have 
# to worry about data processes

## generate list of dataframe names
#df_names = []
#for fname in file_names:    
#    df_names.append(fname[:-4])
#    
#for df in df_names:
#    col_count = len(df.columns)
#    print col_count