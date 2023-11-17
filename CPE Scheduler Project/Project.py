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
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib import style
from matplotlib import rcParams
from matplotlib import rc
from matplotlib import axes


#rcParams['font.family'] = 'sans-serif'
#rcParams['font.sans-serif'] = ['Tahoma']


import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Static data for now
time_ranges = {
    'Monday': [('3:00 PM', '8:00 PM')],
    'Tuesday': [('1:00 PM', '2:00 PM'), ('4:00 PM', '6:00 PM')],
    'Wednesday': [('8:00 AM', '11:00 AM')],
    'Thursday': [('5:00 PM', '8:00 PM')],
    'Friday': [('11:00 AM', '1:00 PM'), ('3:00 PM', '5:00 PM')]
}

# Convert times to matplotlib date-time format
for day, ranges in time_ranges.items():
    for i, (start_time, end_time) in enumerate(ranges):
        start_time = datetime.strptime(start_time, '%I:%M %p')
        end_time = datetime.strptime(end_time, '%I:%M %p')
        time_ranges[day][i] = (mdates.date2num(start_time), mdates.date2num(end_time))

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
            cal.plot([i, i], [start_time, end_time], color='b', linewidth=10) #use solid_capstyle='round' to make the lines rounded. Remove it for square edges.

# X-axis displays days of the week
cal.set_xticks(range(len(days)))
cal.set_xticklabels(days)


plt.show()