import os
import csv

csvpath = os.path.join("..", "Resources", "election_data.csv")

def election_analysis():
    candidates = []
    total_votes = len(list(csvreader))
  
    
    for row in csvreader:
        # total_votes.append(row[0])
        candidates.append(row[2])
  

    print("Election Results")
    print("---------------------")
    print(f'Total Votes: {total_votes}')
    print("---------------------")

with open(csvpath, "r", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    election_analysis()


