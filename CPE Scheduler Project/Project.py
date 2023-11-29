'''
* Calendar visualization project
* Weekly Timetable using python and matplotlib

* For the Career Peer Educator office at Career Centre, University of Alberta

* Author: Saahil Rachh (https://github.com/SAL778)
'''

import calendar # not needed, made on from scratch + matplotlib
import datetime
import time
import sys
import os
import random
import math
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib import style
from matplotlib import rcParams
from matplotlib import rc
from matplotlib import axes
import re


#rcParams['font.family'] = 'sans-serif'
#rcParams['font.sans-serif'] = ['Tahoma']


import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']



import pandas as pd
from datetime import datetime
import matplotlib.dates as mdates

df = pd.read_excel(r"C:\Users\17807\Desktop\STUDIES\_CPE\CPE Scheduler Project\temp.xlsx")  # Load the Excel file
data = df.to_dict('records')    # Read data from the Excel file



# Convert the data into the desired format
time_ranges = {}
for row in data:
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        if day in row and pd.notna(row[day]):
            time_range = row[day].replace(' to ', ' - ').split(' - ') # replace 'to' with '-' for consistency
            #time_range = re.split('\D+', row[day])
            start_time, end_time = time_range[0], time_range[1]
            try:
                start_time = datetime.strptime(start_time, '%I:%M %p')
            except ValueError:
                try:
                    start_time = datetime.strptime(start_time, '%H:%M')
                except ValueError:
                    try:
                        start_time = datetime.strptime(start_time, '%H:%M:%S')
                    except ValueError:
                        start_time = datetime.strptime(start_time + ' PM', '%I:%M %p')
            try:
                end_time = datetime.strptime(end_time, '%I:%M %p')
            except ValueError:
                try:
                    end_time = datetime.strptime(end_time, '%H:%M')
                except ValueError:
                    try:
                        end_time = datetime.strptime(end_time, '%H:%M:%S')
                    except ValueError:
                        end_time = datetime.strptime(end_time + ' PM', '%I:%M %p')
            if day in time_ranges:
                time_ranges[day].append((mdates.date2num(start_time), mdates.date2num(end_time)))
            else:
                time_ranges[day] = [(mdates.date2num(start_time), mdates.date2num(end_time))]


'''
time_ranges = {}
for row in data:
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        if day in row and pd.notna(row[day]):
            time_range = row[day].replace(' to ', ' - ').split(' - ') # replace 'to' with '-' for consistency
            start_time, end_time = time_range[0], time_range[1]
            for time in [start_time, end_time]:
                try:
                    time = datetime.strptime(time, '%I %p')
                    time = datetime.strptime(time, '%I:%M %p')
                    # or time can be of the format %I %p
                    
                except ValueError:
                    try:
                        time = datetime.strptime(time, '%H:%M')
                    except ValueError:
                        try:
                            time = datetime.strptime(time, '%H:%M:%S')
                        except ValueError:
                            if time.isdigit() and len(time) <= 2:  # if time is a single digit or two digits
                                time = datetime.strptime(time + ' PM', '%I %p')
                                #time = datetime.strptime(time + ' PM', '%I:%M %p')
                            else:
                                time = datetime.strptime(time + ' PM', '%I:%M %p')
            if day in time_ranges:
                time_ranges[day].append((mdates.date2num(start_time), mdates.date2num(end_time)))
            else:
                time_ranges[day] = [(mdates.date2num(start_time), mdates.date2num(end_time))]
'''


fig, cal = plt.subplots()

# Y-axis displays time
cal.yaxis_date()
cal.yaxis.set_major_formatter(mdates.DateFormatter('%I:%M %p'))  # hours:minutes
cal.yaxis.set_major_locator(mdates.HourLocator(interval=1))  # tick every hour
cal.yaxis.set_minor_locator(mdates.MinuteLocator(interval=30))   # tick every 30 minutes
cal.invert_yaxis()  # invert y-axis, EOD is origin.



# Plotting each day
for i, day in enumerate(days):
    if day in time_ranges:
        for start_time, end_time in time_ranges[day]:
            cal.plot([i, i], [start_time, end_time], color='b', linewidth=7) # use solid_capstyle='round' to make the lines rounded. Remove it for square edges.
            # thinner line widths give more accurate time plots.

# X-axis displays days of the week
cal.set_xticks(range(len(days)))
cal.set_xticklabels(days)


plt.show()
