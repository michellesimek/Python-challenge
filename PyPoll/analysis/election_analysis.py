#import os module to create paths across operating systems
import os
#import module for reading CSV files

import csv

#path of file we are pulling data from
csvpath = os.path.join("..", "Resources", "election_data.csv")
#path to export results in a textfile
output_path = os.path.join("..", "analysis", "Election_results.txt")

#function to analyze results
def election_analysis():
    
    #set blank list and values before looping through rows in csv
    total_votes = 0
    candidates = []
    candidate_vote = []
    percentages = []
    results = {}
    finale_results = []

    #loop through rows in csv
    for row in csvreader:
        #add 1 after every vote to determine total votes
        total_votes += 1
        #if candidate is not listed in candidate list, add candidate and start tallying up votes
        if row[2] not in candidates:
            #add candidate to list
            candidates.append(row[2])
            #add 1 to start tallying up candidate vote
            candidate_vote.append(1)
            #create index to know position of candidate and their votes in lists
            index = candidates.index(row[2])
        #if candidate is already listed in candidate list, tally up another vote in their specifc running total based on their index(location)
        else:
            #reference location of candidate already in list
            index = candidates.index(row[2])
            #add 1 vote to running tally of votes
            candidate_vote[index] += 1
    
    #loop through each candidate total votes, and find percentages. Add percentages to percentages list
    for number in candidate_vote:
        percentages.append((number / total_votes)*100)

    #add lists to results dictionary
    results["Candidate"] = candidates
    results["Votes"] = candidate_vote
    results["Vote Percentage"] = percentages

    #create a for loop to loop through index (added 1 to grab last candidate) and determine values from result dictionary
    #loop through index and append results to finale_results list
    for x in range(index + 1):
        finale_results.append(f'{results["Candidate"][x]}: {results["Vote Percentage"][x]}% ({results["Votes"][x]})')
    # if statement to find winner based off who had the greatest number of votes
        if results["Votes"][x] == max(candidate_vote):
            winner = results["Candidate"][x]
    
    #print results
    print("Election Results")
    print("---------------------")
    print(f'Total Votes: {total_votes}')
    print("---------------------")
    print('\n'.join(finale_results))
    print("---------------------")
    print(f'Winner: {winner}')

    #export election results to a textfile
    with open(output_path, "w", encoding="utf8") as textfile:
        
        textfile.write(
        "Election Results\n"
        "---------------------\n"
        "Total Votes: "+ str(total_votes) + "\n"
        "---------------------\n")
        
        #print each element in list in a new line
        textfile.write('\n'.join(finale_results) + "\n")

        textfile.write(
        "---------------------\n"
        "Winner: " + (winner) + "\n")

#open csv as read-only to analyze results
with open(csvpath, "r", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #read and skip header row
    csv_header = next(csvreader)

    #call election_analysis function to analyze results
    election_analysis()