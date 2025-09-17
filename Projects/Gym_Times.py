

# This will hopefully be my first decent program
# The goal is to scrape the data from vt's gym website to create a graph of how busy the gyms are at different times of the day
# This project is hopefully going to be a good introduction to webscraping and data visualization
# important: ctrl + c stops program while running

# very important, I used github copilot AI for a large majority of the busy work in this program,
# such as storing and graphing the data once I've scraped it from the vt website
# I will go through every single line and comment in my own words what it does to prove I
# understand and can explain it

from urllib.request import urlopen # imports the library we're going to use to webscrap
import re # a useful module, regular expressions


import matplotlib.pyplot as plt # both of these are graph imports
import numpy as np
plt.close('all')  # Close any existing figures to prevent extra windows

import time # used to get the current time so I can math the data input with a certain time on the graph
from datetime import datetime





from collections import defaultdict # data storage for plotting: map time slot (e.g., 6.25 for 6:15am) to list of values

import pickle # this module helps me save my data after each run of the program so it piles up over time and never gets lost
import os # makes it so the program can interact with my operating system, ie add the file of previous data
DATA_FILE = "gym_times_data.pkl" # Name of the file to store persistent data
war_data_by_time = defaultdict(list)  # {time_slot: [values]} for War Memorial
mc_data_by_time = defaultdict(list)  # {time_slot: [values]} for McComas


# Can be used to clear the pickle file to start fresh, take out comment to run
#if os.path.exists(DATA_FILE):
#	os.remove(DATA_FILE)  # Delete the file if it exists

# Load previous data if it exists
if os.path.exists(DATA_FILE): # checks to see if a data file exists
	with open(DATA_FILE, "rb") as f: # open the file in binary read mode
		data = pickle.load(f) # load the data from the file
		war_data_by_time.update(data.get("war", {})) # update War Memorial data
		mc_data_by_time.update(data.get("mc", {})) # update McComas data

def scrape_occupancy():
	url = "https://connect.recsports.vt.edu/facilityoccupancy" # URL to scrape
	page = urlopen(url) # Open the webpage
	html_bytes = page.read() # Read HTML content
	html = html_bytes.decode("utf-8") # Decode bytes to string
	results = (re.findall("Current Occupancy: ..", html)) # finds all instances of current occupancy: the two periods can act as any character
	war = int(results[0][19] + results[0][20]) # Extract War Memorial occupancy
	mc = int(results[3][19] + results[3][20]) # Extract McComas occupancy
	return war, mc # Return both values


# Detect if today is a weekend
today = datetime.now().weekday()  # 0=Monday, 6=Sunday
is_weekend = today >= 5  # Saturday or Sunday

# Set up x-axis and tick labels depending on weekend/weekday
if is_weekend:
	# Weekend: McComas 8am-8pm, WMH 10am-10pm
	x_labels = ["8am", "10am", "12pm", "2pm", "4pm", "6pm", "8pm"]
	x = np.arange(8, 21, 2)  # 8am to 8pm, every 2 hours
else:
	# Weekday: McComas 6am-10pm, WMH 5am-11pm
	x_labels = ["6am", "8am", "10am", "12pm", "2pm", "4pm", "6pm", "8pm", "10pm"]
	x = np.arange(6, 23, 2)  # 6am to 10pm, every 2 hours

# Set up y-axis: 0% to 100% with 4 even intervals

y_labels = ["0%", "25%", "50%", "75%", "100%"] # Y-axis labels
y = np.linspace(0, 100, 5) # Y-axis tick positions


# Create a single window with two subplots side by side

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5)) # Create two subplots side by side


def update_plots():
	ax1.clear()  # Clear the first subplot for fresh drawing
	ax2.clear()  # Clear the second subplot for fresh drawing

	# Prepare sorted time slots and averages for plotting
	if mc_data_by_time:
		mc_times = sorted(mc_data_by_time.keys())
		mc_avgs = [sum(mc_data_by_time[t])/len(mc_data_by_time[t]) for t in mc_times]
		ax1.plot(mc_times, mc_avgs, 'ro-', label='McComas (avg)')  # Plot average McComas data
	ax1.set_xticks(x)  # Set x-axis tick positions (more ticks)
	ax1.set_xticklabels(x_labels)  # Set x-axis tick labels (more labels)
	ax1.set_yticks(y)  # Set y-axis tick positions
	ax1.set_yticklabels(y_labels)  # Set y-axis tick labels
	ax1.set_xlim(6, 22)  # Set x-axis limits
	ax1.set_ylim(0, 100)  # Set y-axis limits
	ax1.set_xlabel("Time of Day")  # Label x-axis
	ax1.set_ylabel("Occupancy (%)")  # Label y-axis
	ax1.set_title("McComas Gym Occupancy (Averaged)")  # Set plot title
	ax1.grid(True, which='both', axis='both', linestyle='--', alpha=0.5)  # Add grid lines

	if war_data_by_time:
		war_times = sorted(war_data_by_time.keys())
		war_avgs = [sum(war_data_by_time[t])/len(war_data_by_time[t]) for t in war_times]
		ax2.plot(war_times, war_avgs, 'bo-', label='War Memorial (avg)')  # Plot average War Memorial data
	# Set x-axis for War Memorial depending on weekend/weekday
	if is_weekend:
		x2_labels = ["10am", "12pm", "2pm", "4pm", "6pm", "8pm", "10pm"]
		x2 = np.arange(10, 23, 2)  # 10am to 10pm, every 2 hours
		ax2.set_xlim(10, 22)
	else:
		x2_labels = ["5am", "7am", "9am", "11am", "1pm", "3pm", "5pm", "7pm", "9pm", "11pm"]
		x2 = np.arange(5, 24, 2)  # 5am to 11pm, every 2 hours
		ax2.set_xlim(5, 23)
	ax2.set_xticks(x2)  # Set x-axis tick positions
	ax2.set_xticklabels(x2_labels)  # Set x-axis tick labels and rotate
	ax2.set_yticks(y)  # Set y-axis tick positions
	ax2.set_yticklabels(y_labels)  # Set y-axis tick labels
	ax2.set_xlim(5, 23)  # Set x-axis limits
	ax2.set_ylim(0, 100)  # Set y-axis limits
	ax2.set_xlabel("Time of Day")  # Label x-axis
	ax2.set_ylabel("Occupancy (%)")  # Label y-axis
	ax2.set_title("War Memorial Gym Occupancy (Averaged)")  # Set plot title
	ax2.grid(True, which='both', axis='both', linestyle='--', alpha=0.5)  # Add grid lines
	plt.tight_layout()  # Adjust layout to prevent overlap
	plt.draw()  # Redraw the current figure with updates
	plt.pause(0.1)  # Pause to allow the plot window to update




def get_time_slot():
	now = datetime.now()
	# Round to nearest 5 minutes (0.0833 hour)
	slot = now.hour + round(now.minute/5)*(5/60)
	return slot



def collect_and_update():
	slot = get_time_slot()
	war, mc = scrape_occupancy()
	war_data_by_time[slot].append(war)
	mc_data_by_time[slot].append(mc)
	update_plots()
	# Save data after each update
	with open(DATA_FILE, "wb") as f:
		pickle.dump({"war": dict(war_data_by_time), "mc": dict(mc_data_by_time)}, f)
	# Schedule the next update in 5 minutes (300,000 ms)
	timer = fig.canvas.new_timer(interval=300000)
	timer.add_callback(collect_and_update)
	timer.start()

# Start the first update
collect_and_update()

try:
	plt.show()
except KeyboardInterrupt:
	# Save data one last time on exit
	with open(DATA_FILE, "wb") as f:
		pickle.dump({"war": dict(war_data_by_time), "mc": dict(mc_data_by_time)}, f)
	print("Data saved. Exiting.")


#below is all attempted code, left in too see what I tried and how I ended up using something better

#wmh_index = html.find("Current Occupancy: ")
#wmh_num = wmh_index + 19
#print(html[wmh_num:wmh_num+2])
#mc_index = html[wmh_num:].find("Current Occupancy: ")
#print(mc_index)