#You will need to install the FFMpeg library : pip install ffmpeg

import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

#All data courtesy of the Federeral Reserve Bank of St Louis. https://fred.stlouisfed.org/


#Read in data 
fed_funds= pd.read_csv('fed_funds_rate.csv').rename(columns={'DATE': "Time",'FEDFUNDS': 'fed_funds_rate'}).set_index('Time')
unemployment=pd.read_csv('us_unemployment.csv').rename(columns={'DATE': "Time",'UNRATE': 'unemployment_rate'}).set_index('Time')
housing=pd.read_csv('case_pc.csv').rename(columns={'DATE': "Time",'CSUSHPISA_PCH': 'case_shiller'}).set_index('Time')

#Slice data to required time frame
fed_funds=fed_funds.loc['2000-08-01':'2010-11-01',:]
unemployment=unemployment.loc['2000-08-01':'2010-11-01',:]
housing=case_shiller.loc['2000-08-01':'2010-11-01',:]
 
#Convert index to datetime
fed_funds.index = pd.to_datetime(fed_funds.index)
unemployment.index = pd.to_datetime(unemployment.index)
housing.index = pd.to_datetime(housing.index)
 
#Define the data variables for the chart 
fed=fed_funds[['fed_funds_rate']]
housing =case_shiller[["case_shiller"]] 
unemployment =unemployment[['unemployment_rate']] 


#Define the date range for x axis in chart
dates = pd.date_range(start='2000-08-01', end='2010-11-01', freq='MS')

 
# Define the figure and axis
fig, ax = plt.subplots(figsize=(9, 4))

# Define the function to animate the plot
def animate(i):
    ax.clear()
    
    #Background color
    ax.set_facecolor('#1075A0')
    
    #plot unemployment rate
    ax.plot(dates[:i+1], unemployment[:i+1],'white', label='US Unemployment Rate', linewidth=1)
    
     
    #Plot Fed Funds Rate
    ax.plot(dates[:i+1], fed[:i+1],'#7792E3', label='Fed Funds Rate', linewidth=4, marker='.')
    
    #Plot US house prices(Case Shiller) 
    ax.plot(dates[:i+1], housing[:i+1],'black', label='US House Prices(monthly % change)', linewidth=1)
    
    #Title
    ax.set_title('GFC') 
    
    #Define x and y axis upfront so axis will not jump around as data is read in.
    ax.set_ylim([-5, 11])
    ax.set_xlim([dates[0], dates[-1]])
    
    
    ax.legend()
     

# Create the animation and produce an mp4 file in the local directory called "fomc_gfc.mp4"
writer = FFMpegWriter(fps=5,codec='mpeg4')
with writer.saving(fig, "fomc_gfc.mp4",100):
    for i in range(len(dates)):
        animate(i)
      
        writer.grab_frame()
