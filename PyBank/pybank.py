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
    #print(f"CSV Header: {csv_header}")

# read each row of data after the header and append to list while incrementing the month count
    for row in csvreader:
        months = months + 1
        #print(row)
        date.append(row[0])
        profloss.append(float(row[1]))
        
#for debugging purposes
#print(date)
#print(profloss)

#set totalprof to the first profloss number
totalprof = profloss[0]

#set variables
#set highest and lowest to extreme numbers to start with just in case every month is either higher or greater than zero
#setting to zero still works for this data set though
totalchange = 0
highest = -1000000
lowest = 1000000

#for debugging purposes
#print(f" total prof:  {totalprof}")

#start at 1 since we already set totalprof to the first number to determine the change each month
for n in range (1, months):

    #calculate total amount of profit/loss by adding each month's amount to the total
    totalprof = totalprof + profloss[n]
    
    #calculate total change
    change = profloss[n] - profloss[n-1]
    totalchange = totalchange + change
    
    #calculate greatest increase and grab matching month
    if change > highest:
        highest = change
        month_h = date[n]

    #calculate greatest decrease and grab matching month
    elif change < lowest:
        lowest = change
        month_l = date[n]

#for debugging purposes
#print(f"highest: {highest}")
#print(f"highest month: {month_h}")
#print(f"lowest: {lowest}")
#print(f"lowest month: {month_l}")

#display the financial analysis in terminal
print(f" ")
print(f" ")
print(f"Financial Analysis")
print(f"-------------------------------")
print(f"Total Months: {months}")
print(f"Total: ${int(totalprof)}")
print(f"Average Change: ${round((totalchange/(months - 1)), 2)}")
print(f"Greatest Increase in Profits: {month_h} (${int(highest)})")
print(f"Greatest Decrease in Profits: {month_l} (${int(lowest)})")

#output the analysis.txt file to the Analysis folder
with open("Analysis/Analysis.txt","w") as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"-------------------------------\n")
    txtfile.write(f"Total Months: {months}\n")
    txtfile.write(f"Total: ${int(totalprof)}\n")
    txtfile.write(f"Average Change: ${round((totalchange/(months - 1)), 2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {month_h} (${int(highest)})\n")
    txtfile.write(f"Greatest Decrease in Profits: {month_l} (${int(lowest)})\n")
