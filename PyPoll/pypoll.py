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
        #if the candidate is not on the list, add them and give them a vote
        if candidate.count(row[2]) == 0:
        	candidate.append(row[2])
        	votes.append(1)
        #if the candidate is already on the list, just give them a vote
        else:
        	votes[candidate.index(row[2])] = votes[candidate.index(row[2])] + 1


#for debugging purposes
# Voter ID, County, Candidate
#print(f"{candidate[0]}")
#print(candidate)
#print(votes)
#print(type(votes))
#print(type(num_votes))
#print(f"{range(len(candidate))}")

#display the results in terminal
print(f" ")
print(f" ")
print(f"Election Results")
print(f"-------------------------------")
print(f"Total Votes: {num_votes}")
print(f"-------------------------------")

#calculate the percentage for each candidate and print candidate, percent, and vote count
for x in range(len(candidate)):
	vote_p = ((votes[x]/num_votes)*100)
	print(f"{candidate[x]}: {round(vote_p):.3f}% ({votes[x]})")
print(f"-------------------------------")

#calculate the winner and display their name
#set new variable to zero for the number of votes of the winning candidate
win_votes = 0

#check each candidate's vote count and set the coresponding name as winner if their count is higher
for y in range(len(candidate)):
	if votes[y] > win_votes:
		winner = candidate[y]
		win_votes = votes[y]
print(f"Winner: {winner}")
print(f"-------------------------------")

#output the results.txt file to the Analysis folder