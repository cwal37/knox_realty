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

filter_walk(source_directory, output_directory, 'RegionName', 37917)

file_names = file_walk(os.getcwd())
