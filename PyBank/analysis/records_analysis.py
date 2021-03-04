#import os module to create paths across operating systems
import os

#import module for reading CSV files
import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")

#open file as read-only
with open(csvpath, 'r', encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    for row in csvreader:
        print(row)

