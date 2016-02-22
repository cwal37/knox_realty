# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 16:45:05 2016

@author: Connor
"""
import os
import pdb
import pandas as pd
from file_walk_with_me import *
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import FontProperties
import matplotlib.patheffects as path_effects


plt.close()
mpl.rcdefaults()
mpl.rcParams['figure.figsize'] = 14, 9
plt.style.use('ggplot')
mpl.rcParams.update({'font.size': 9})


# location of unscrubbed (for knoxville) realty data, hundreds of MB, so excluded
# from the repo, you can find th files from zillow on their data page
source_directory = 'C:\Users\lp0ougx3\Desktop\Development\knox_realty\wanted_data'
output_directory = 'C:\Users\lp0ougx3\Desktop\Development\knox_realty\\filtered_data'

# run filter walk when you need to generate new filtered files, otherwise it's
# just an overhead on the whole script running

filter_walk(source_directory, output_directory, 'RegionName', 37917)

file_names = file_walk(output_directory)

"""
0 Buyer/Seller Index: This index combines the sale-to-list price ratio, 
the percent of homes that subject to a price cut and the time properties 
spend on the market (measured as Days on Zillow). Higher numbers indicate a 
better buyers’ market, lower numbers indicate a better sellers’ market, 
relative to other markets within a metro.
1 Inventory Smooth, Seasonally adjusted (seasonally adjusted using the X-12-Arima method) 
2 Inventory (Raw): Median of weekly snapshot of for-sale homes within a region for a given month.
3 Market Health Index: This index indicates the current health of a given region’s 
housing market relative to other markets nationwide. It is calculated on a scale 
from 0 to 10, with 0 representing the least healthy markets and 10 the healthiest markets.
4 Sales
5 Ratio of Homes sold as foreclosures to all homes
6 Listings With Price Cut (%): The percentage of current listings on Zillow
 with a price cut during the month, seasonally adjusted, single family residence.
7 3 bedroom Median List Price Per Sq Ft ($): Median of list prices divided by the square footage of a home.
8 single family residence bedroom Median List Price Per Sq Ft ($): Median of list prices divided by the square footage of a home.
9 median price per 3 bedroom $
10 median price sfr $
11 Median price cut (%): Median of the percentage price reduction for homes with a price reduction during the month. SFR
12 single family residence bedroom Median Sold Price Per Sq Ft ($): Median of list prices divided by the square footage of a home.
13 sfr median price cut dollar
14 Decreasing Values (%): The percentage of homes in an given region with values that have decreased in the past year.
15 Increasing Values (%): The percentage of homes in an given region with values that have decreased in the past year.
16 SFR Listings With Price Cut (%): The percentage of current listings on Zillow with a price cut during the month.
17 Foreclosure Re-Sales (%): The percentage of home sales in a given month in which the home was foreclosed upon 
within the previous year (e.g. sales of bank-owned homes after the bank took possession of a home following a foreclosure).
18 Sold in Past Year (Turnover) (%): The percentage of all homes in a given area that sold in the past 12 months.
19 ???
20 ZHVI 2 bdrm
21 ZHVI 3 bdrm
22 ZHVI SFR
23 
"""

# dictionary format for graphing labels and such
# file_name_dict = {fileNames[0]:[xlabel, ylabel, title], }

file_name_dict = {file_names[0]:['Date', 'Index Value', 'Buyer/Seller Index'],file_names[1]:['Date', 'Number Available', 'Inventory Smooth, Seasonally adjusted'],
                  file_names[2]:['Date', 'Number Available', 'Median of weekly snapshot of for-sale homes within a region for a given month'],file_names[3]:['Date', 'Index Value', 'Market Health Index (0 least healthy, 10 most)'],
                  file_names[4]:['Date', 'Number Sold', 'All Homes Sold'],file_names[5]:['Date', 'Ratio', 'Ratio of Homes Sold as Foreclosures to All Homes'],
                  file_names[6]:['Date', '%', 'Percentage of Listings with a Price Cut during the Month'],file_names[7]:['Date', '$/square foot', '3 Bedroom Median List Price Per Sq Ft'],
                  file_names[8]:['Date', '$/square foot', 'Single Family Residence Median List Price Per Sq Ft'],file_names[9]:['Date', '$', 'Median Price for 3 Bedroom Homes'],
                  file_names[10]:['Date', '$', 'Median Price for Single Family Residences'],file_names[11]:['Date', 'Percent (%)', 'Median of the percentage price reduction for homes with a price reduction during the month'],
                  file_names[12]:['Date', '$', 'Single Family Residence Median Sold Price Per Sq Ft'],file_names[13]:['Date', '$', 'Single Family Residence Median Price Cut'],
                  file_names[14]:['Date', 'Percent (%)', 'Percentage of homes in an given region with values that have decreased in the past year'],file_names[15]:['Date', 'Percent (%)', 'Percentage of homes in an given region with values that have increased in the past year'],
                  file_names[16]:['Date', 'Percent (%)', 'The percentage of current Single Family Residence listings on Zillow with a price cut during the month'],file_names[17]:['Date', 'Percent (%)', 'Percent of Foreclosure Re-Sales'],
                  file_names[18]:['Date', 'Percent (%)', 'Percent Sold in Past Year (Turnover)'],file_names[19]:['Date', 'Count', 'UnsoldReos_All_Homes'],
                  file_names[20]:['Date', 'ZHVI', '3 Bedroom ZHVI'],file_names[21]:['Date', 'ZHVI', 'Single Family Residence, ZHVI per Square Foot']}


graph_output_directory = 'C:\Users\lp0ougx3\Desktop\Development\knox_realty\\results\\'

if not os.path.exists(graph_output_directory):
    os.makedirs(graph_output_directory)    


# generate dataframes for all files from the filtered files, then some graphing    
for fname in file_names:
    plt.close()
    df = pd.read_csv(output_directory + '\\' + fname)
    col_count = len(df.columns)
    if df.columns[col_count-1] != '2015-12':
        print "Not time series data"
    else:
        y = range(0,36)
        x = []
        #print fname
        labels = df.columns[col_count-36:col_count]
        for i in range(col_count-36,col_count):
            #print i
            #pdb.set_trace()
            x.append(df.ix[0][i])
        
        #y = [y+0.5 for y in y]        
        
        plt.plot(y,x, linewidth = 4)
        plt.xlabel(file_name_dict[fname][0])
        plt.ylabel(file_name_dict[fname][1])
        plt.xticks(y, labels, rotation=45)
        if fname[0:3] == 'Zip':
            
            #plt.title(fname[4:-4]+' '+df.columns[col_count-37]+' to '+df.columns[col_count-1])
            plt.title(file_name_dict[fname][2])
            plt.savefig(graph_output_directory+fname[4:-4]+'.png', dpi = 300)
        else:
            plt.title(file_name_dict[fname][2])
            plt.savefig(graph_output_directory+fname[:-4]+'.png', dpi = 300)          



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