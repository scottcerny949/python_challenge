import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "PyPoll_Resources_election_data.csv")


# create lists to store data
candidate = []
votes = []
num_votes = 0


# read in the csv file
with open(csvpath, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # read each row of data after the header and append to list while incrementing the vote count
    for row in csvreader:
        num_votes = num_votes + 1
        #print(row)
        if candidate.count(row[2]) == 0:
        	candidate.append(row[2])
        	votes.append(1)
        else:
        	votes[candidate.index(row[2])] = votes[candidate.index(row[2])] + 1


# Voter ID, County, Candidate

#print(f"{candidate[0]}")

for y in range(len(candidate)):
	print(f"{votes[y]/num_votes}")



print(candidate)
print(votes)

print(f" ")
print(f" ")
print(f"Election Results")
print(f"-------------------------------")
print(f"Total Votes: {num_votes}")
print(f"-------------------------------")
for x in range(len(candidate)):
	print(f"{candidate[x]}: {votes[x]}")
print(f"-------------------------------")
print(f"Winner: ")
print(f"-------------------------------")
