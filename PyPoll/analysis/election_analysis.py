import os
import csv

csvpath = os.path.join("..", "Resources", "election_data.csv")
output_path = os.path.join("..", "analysis", "Election_results.txt")

#function to analyze results
def election_analysis():
    
    candidates = []
    total_votes = 0
    candidate_vote = []
    percentages = []
    results = {}

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
        #if candidate is already listed in candidate list, tally up another vote in their running total
        else:
            #reference location of candidate already in list
            index = candidates.index(row[2])
            #add 1 vote to running tally of votes
            candidate_vote[index] += 1
    
    for number in candidate_vote:
        percentages.append((number / total_votes)*100)
   
    results["Candidate"] = candidates
    results["Votes"] = candidate_vote
    results["Vote Percentage"] = percentages

    print("Election Results")
    print("---------------------")
    print(f'Total Votes: {total_votes}')
    print("---------------------")
    # print(candidates)
    # print(candidate_vote)
    # print(percentages)
    # print(f'{results["Candidate"][0]}: {results["Vote Percentage"][0]}%  ({results["Votes"][0]})')
    # print(f'{results["Candidate"][1]}: {results["Vote Percentage"][1]}%  ({results["Votes"][1]})')
    # print(f'{results["Candidate"][2]}: {results["Vote Percentage"][2]}%  ({results["Votes"][2]})')
    # print(f'{results["Candidate"][3]}: {results["Vote Percentage"][3]}%  ({results["Votes"][3]})')
    #create a for loop to loop through index (added 1 to grab last candidate) and determine values from result dictionary
    for x in range(index + 1):
        print(f'{results["Candidate"][x]}: {results["Vote Percentage"][x]}% ({results["Votes"][x]})')


    #export election results to a textfile
    with open(output_path, "w", encoding="utf8") as textfile:
        textfile.write(
        "Election Results\n"
        "---------------------\n"
        "Total Votes: "+ str(total_votes) + "\n"
        "---------------------\n"
        "Candidates: " + str(candidates) + "\n"
        "Votes: " + str(candidate_vote) + "\n"
        "Vote Percentage: " + str(percentages) + "\n")


#open csv as read-only to analyze results
with open(csvpath, "r", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip headers
    csv_header = next(csvreader)

    #call function to analyze results
    election_analysis()