#import modules
import os
import csv

#set path for the data
csvpath=os.path.join("Resources","Election_data.csv")

# Set variables to hold total votes
total_votes = 0

# set a list for for candidates
candidate_list = []

# set a list to hold votes the candidas receive
vote_count = []

# list to hold percentage
percentage_list = []


# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header first 
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        # count the total number of votes
        total_votes += 1

        # add the candidate's name to candidate list when it first appears
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            vote_count.append(1)

        # if it's already in the list, add 1 to the candidate's name   
        else:
            vote_count[candidate_list.index(row[2])] += 1

# Calculate percent of vote            
percentage_list = [(100/total_votes) * x for x in vote_count]

# Find the winner
winner = candidate_list[vote_count.index(max(vote_count))]

# Print the result      
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")

for x in candidate_list:
    print(x + ": " + str(format(percentage_list[candidate_list.index(x)], '.3f')) 
        + "% (" + str(vote_count[candidate_list.index(x)]) + ")")
    
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

# Write to text file
f = open("analysis.txt", "w")

f.write("Election Results\n")
f.write("-------------------------\n")
f.write("Total Votes: " + str(total_votes) + "\n")
f.write("-------------------------\n")

for x in candidate_list:
    f.write(x + ": " + str(format(percentage_list[candidate_list.index(x)], '.3f')) 
        + "% (" + str(vote_count[candidate_list.index(x)]) + ")\n")
    
f.write("-------------------------\n")
f.write("Winner: " + winner + "\n")
f.write("-------------------------\n")

f.close()




        
