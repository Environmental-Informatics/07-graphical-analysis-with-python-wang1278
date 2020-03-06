"""
Creator: Linji Wang (wang1278)
Date of Creation: 03/06/20
File Name: program-07.py
Discription:
    This script is for graphical analysis of earthquake data for the past 30
    days retrived from USGS
"""

# import necessary libararies for .csv data processing and plotting
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# import data from .csv file,  remove all null data, and reset index
eqdata=pd.read_table('all_month.csv',sep=',',usecols=['time','latitude','longitude','mag','depth'])
eqdata=eqdata.dropna()
eqdata=eqdata.reset_index(drop=True)

# Generate a histogram of earthquake magnitude, using a bin width of 1 and a range of 0 to 10
plt.hist(eqdata['mag'],bins=10,width=1,range=(0,10),density=True)
plt.title('Earthquake Magnitude Histogram')
plt.xlabel('Magnitude')
plt.ylabel('Density')
plt.savefig('Histogram of Earthquake Magnitude.jpg') # save the figure for uses in metadata file
plt.close()

# Convert data to gaussian kernel with a kernel width of 0.5
eqdata_kde=stats.gaussian_kde(eqdata['mag'])
eqdata_kde.covariance_factor=lambda:0.5
eqdata_kde._compute_covariance()

# Plot KDE
plt.plot(np.sort(eqdata['mag']),eqdata_kde(np.sort(eqdata['mag'])))
plt.title('Earthquake Magnitude KDE')
plt.xlabel('Magnitude')
plt.ylabel('Density')
plt.savefig('KDE of Earthquake Magnitude.jpg')
plt.close()

# plot for latitude and longitude
plt.scatter(eqdata['longitude'],eqdata['latitude'],)
plt.title('Earthquake Locations')
plt.xlabel('Longitude (degree)')
plt.ylabel('Latitude (degree)')
plt.savefig('Earthquake Location.jpg')
plt.close()

# Plot normalized CDF of earthquake depths
plt.plot(np.sort(eqdata['depth']),np.linspace(0,1,len(eqdata['depth'])))
plt.title('Normalized CDF of Earthquake Depth')
plt.xlabel('Depth (km)')
plt.ylabel('Cumulative Density')
plt.savefig('Normalized CDF of Earthquake Depth.jpg')
plt.close()

# Plot for magnitude and depth
plt.scatter(eqdata['mag'],eqdata['depth'])
plt.title('Earthquake Magnitude with Depth')
plt.xlabel('Magnitude')
plt.ylabel('Depth (km)')
plt.savefig('Earthquake Magnitude with Depth.jpg')
plt.close()

# Q-Q Plot for earthquake magnitude
stats.probplot(eqdata['mag'],plot=plt)
plt.title('Q-Q Plot of Earthquake Magnitude')
plt.xlabel('Normal Distribition')
plt.ylabel('Earthquake Magnitude')
plt.savefig('Q-Q Plot of Earthquake Magnitude.jpg')
plt.close()
