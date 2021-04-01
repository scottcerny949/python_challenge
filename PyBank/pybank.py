import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources",  "budget_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")






#calculate total number of months


#calculate total amount of profit/loss


#calculate average change


#calculate greatest increase


#calculate greatest decrease


#export to text file in Analysis folder