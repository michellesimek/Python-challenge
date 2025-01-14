#import os module to create paths across operating systems
import os

#import module for reading CSV files
import csv

#path of file we are pulling data from
csvpath = os.path.join("..", "Resources", "budget_data.csv")
#path to export results in a textfile
output_path = os.path.join("..", "analysis", "PyBank_results.txt")


#function to return analysis for dataset
def dataset_analysis():

    #set blank lists and values before looping through rows in csv
    total_months = []
    total_amount = 0

    #set blank lists and values before looping and finding change amount 
    change_amount = 0
    previous_amount = 0
    change_list = []

    
    #for loop to read each row in csv
    for row in csvreader: 
        
        #find number of months and new total amount of Profits/Losses
        total_months.append(row[0])
        total_amount += int(row[1])
        
        #Determine average of changes in profits
        change_amount = int(row[1]) - (previous_amount)
        previous_amount = int(row[1])
        change_list.append(change_amount)

        #find which months the greatest increast and greatest decrease amounts belong to
        if change_amount == max(change_list):
            greatest_month = row[0]
        if change_amount == min(change_list):
            loss_month = row[0]
        
    #find average revenue change from change_list
    average_change = round((sum(change_list)) / (len(change_list)),2)
    #find greatest increase and greastest decrease in change
    greatest_profit = max(change_list)
    greatest_loss = min(change_list)

    
    #print results 
    print(f"Finanical Analysis")
    print('----------------------------------------')
    print(f'Total Months: {len(total_months)}')
    print(f'Total: ${total_amount}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {greatest_month} $({greatest_profit})')
    print(f'Greatest Decrease in Profits: {loss_month} $({greatest_loss})')

    #write results to a textfile
    with open(output_path, 'w', encoding = 'utf8') as textfile:

        #write the results found above
        textfile.write(
        "Finanical Analysis\n"
        '----------------------------------------\n'
        'Total Months: ' + str(len(total_months)) + '\n'
        'Total: ' + str(total_amount) + '\n'
        'Average Change: $ ' + str({average_change,}) + '\n'
        'Greatest Increase in Profits: ' + (greatest_month) + ' $(' + str(greatest_profit) + ')' + '\n'
        'Greatest Decrease in Profits: ' + (loss_month) + ' $(' + str(greatest_loss) + ')' + '\n')

#open csvfile as read only
with open(csvpath, 'r', encoding='utf8') as csvfile:
    #read csvfile with a comma being the delimiter 
    csvreader = csv.reader(csvfile, delimiter=',')

    #read and skip header row
    csv_header = next(csvreader)

    #call dataset_analysis function to find results
    dataset_analysis()

