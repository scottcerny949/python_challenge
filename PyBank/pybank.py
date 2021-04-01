import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# create places to store data
date = []
profloss = []


# with open(udemy_csv, newline='', encoding='utf-8') as csvfile:
with open(csvpath, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header and append to list
    for row in csvreader:
    	date.append(row[0])
#    	print(row[0])
    	profloss.append(row[1])
#    	print(row[1])

#    print(date)
#    print(profloss)
#    print(len(date))


print(f" ")
print(f" ")
print(f" ")
print(f"Financial Analysis")
print(f"-------------------------------")
print(f"Total Months: {len(date)}")


#    	date.append(row[0])
#    	profloss.append(row[1])

#cleaned_csv = zip(date, profloss)

#print(cleaned_csv)

#for row in cleaned_csv:
#	print(row)




#rows = len(group1)
#columns = len(group1[0])

#calculate total number of months


#calculate total amount of profit/loss


#calculate average change


#calculate greatest increase


#calculate greatest decrease


#export to text file in Analysis folder