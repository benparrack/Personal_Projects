# This will hopefully be my first decent program
# The goal is to scrape the data from vt's gym website to create a graph of how busy the gyms are at different times of the day
# This project is hopefully going to be a good introduction to webscraping and data visualization
# important: ctrl + c stops program while running

from urllib.request import urlopen # imports the library we're going to use to webscrap
import re # a useful module, regular expressions


import matplotlib.pyplot as plt # both of these are graph imports
import numpy as np

import time # used to get the current time so I can math the data input with a certain time on the graph
from datetime import datetime





from collections import defaultdict # data storage for plotting: map time slot (e.g., 6.25 for 6:15am) to list of values

import pickle # this module helps me save my data after each run of the program so it piles up over time and never gets lost
import os # makes it so the program can interact with my operating system, ie add the file of previous data
DATA_FILE = "gym_times_data.pkl" # Name of the file to store persistent data
war_data_by_time = defaultdict(list)  # {time_slot: [values]} for War Memorial
mc_data_by_time = defaultdict(list)  # {time_slot: [values]} for McComas

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

# Set up x-axis: 6am to 10pm with 4 even intervals

x_labels = ["6am", "10am", "2pm", "6pm", "10pm"] # X-axis labels for McComas
x = np.linspace(6, 22, 5)  # X-axis tick positions for McComas (6am to 10pm)

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
	ax1.set_xticks(x)  # Set x-axis tick positions
	ax1.set_xticklabels(x_labels)  # Set x-axis tick labels
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
	x2_labels = ["5am", "9am", "1pm", "5pm", "9pm", "11pm"]  # X-axis labels for second plot
	x2 = np.linspace(5, 23, 6)  # X-axis tick positions for second plot
	ax2.set_xticks(x2)  # Set x-axis tick positions
	ax2.set_xticklabels(x2_labels)  # Set x-axis tick labels
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
	# Round to nearest 15 minutes (0.25 hour)
	slot = now.hour + round(now.minute/15)*0.25
	return slot

# using a try except statement so if I exit the program with ctrl + c the data will be saved
try:
	while True:
		now = datetime.now()
		hour_decimal = now.hour + now.minute/60
		slot = get_time_slot()
		war, mc = scrape_occupancy()
		war_data_by_time[slot].append(war)
		mc_data_by_time[slot].append(mc)
		update_plots()
		# Save data after each update
		with open(DATA_FILE, "wb") as f:
			pickle.dump({"war": dict(war_data_by_time), "mc": dict(mc_data_by_time)}, f)
		time.sleep(900)  # Wait 15 minutes
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