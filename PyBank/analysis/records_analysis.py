#import os module to create paths across operating systems
import os

#import module for reading CSV files
import csv

#path of file we are pulling
csvpath = os.path.join("..", "Resources", "budget_data.csv")

#function to return analysis for dataset
def dataset_analysis(row):
    #find the total number of months included in the dataset
    #create an empty list
    total_months = []
    #for each row in the csv, add the month to the total_months list
    for row in csvreader:
        total_months.append(row[0])
    #print the length of total_months list to determine total number of months
    print(f'Total Months: {len(total_months)}')
    
    # total_months = 0
    # total_months = total_months + month
    # total_profit_loss = 0
    # for row in csvreader: 
    #     total_profit_loss = total_profit_loss + profit_loss
    # average = total_profit_loss/months
    # print(profit_loss)
    # print(profit_loss)

    # print(total_profit_loss)

#open file as read-only
with open(csvpath, 'r', encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    print(f"Finanical Analysis")
    print('----------------------------------------')

    for row in csvreader:
        # print(row)
        dataset_analysis(row)
        
