#import os module to create paths across operating systems
import os

#import module for reading CSV files
import csv

#path of file we are pulling
csvpath = os.path.join("..", "Resources", "budget_data.csv")

#function to return analysis for dataset
def dataset_analysis(row):

    total_months = []
    profits_losses = []
    total_amount = 0
    
    for row in csvreader:
        #add each month to total_months list
        total_months.append(row[0])
        #add profit/losses to the profit_losses list
        profits_losses.append(int(row[1]))
        #add profit/losses to total net amount
        total_amount += int(row[1])
        average_change = total_amount/(len(total_months))
        greatest_profit = max(profits_losses)
        greatest_lost = min(profits_losses)

    
    print(f'Total Months: {len(total_months)}')
    print(f'Total: ${total_amount}')
    print(f'Average Change: ${round(average_change,2)}')
    print(f'Greatest Increase in Profits: ${greatest_profit}')
    print(f'Greatest Decrease in Profits: ${greatest_lost}')



with open(csvpath, 'r', encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    print(f"Finanical Analysis")
    print('----------------------------------------')

    for row in csvreader:
        dataset_analysis(row)

