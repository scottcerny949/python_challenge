import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# create lists to store data
# set months to zero to start

months = 0
date = []
profloss = []


# read in the csv file
with open(csvpath, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")

# Read each row of data after the header and append to list while incrementing the month count
    for row in csvreader:
        months += 1
        #print(row)
        date.append(row[0])
        profloss.append(float(row[1]))
        
#print(date)
#print(profloss)
#set totalprof to the first profloss number
totalprof = profloss[0]
#set variables to zero
totalchange = 0
highest = 0
lowest = 0

#print(profloss[0])
#print(f" total prof:  {totalprof}")

#start at 1 since we already grabbed 0 to determine the change each month

for n in range (1, months):
    #calculate total amount of profit/loss
    totalprof += profloss[n]
    
    #calculate average change
    change = profloss[n] - profloss[n-1]
    totalchange += change
    
    #calculate greatest increase
    if change > highest:
        highest = change
        month_h = date[n]
    #calculate greatest decrease    
    elif change < lowest:
        lowest = change
        month_l = date[n]

#print(f"highest: {highest}")
#print(f"lowest: {lowest}")

#display the financial analysis in terminal
print(f" ")
print(f" ")
print(f" ")
print(f"Financial Analysis")
print(f"-------------------------------")
print(f"Total Months: {months}")
print(f"Total: ${totalprof}")
print(f"Average Change: ${(totalchange/(months - 1))}")
print(f"Greatest Increase in Profits: {month_h} (${highest})")
print(f"Greatest Decrease in Profits: {month_l} (${lowest})")

#output the financial analysis to file in the Analysis folder

