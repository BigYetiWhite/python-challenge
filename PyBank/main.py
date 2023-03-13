
#Import modules for .csv files
import os
import csv


# Locate and connect to our data source
bank_data_csv = os.path.join("..", "PyBank", "Resources", "budget_data.csv")



# Open and print the data in the file
with open(bank_data_csv) as bank_data_file:
    file_reader = csv.reader(bank_data_file, delimiter=",")

    csv_header = next(bank_data_file)


#Containers for variable data to be stored
    count=0
    Total=0
    last_profit_loss=0
    first=True
    Max_change=0
    Min_change=0
    Date_of_Max=""
    Date_of_Min=""
    Total_Change=0

#Looping of Data for All Value Responses
    for data_row in file_reader:
        count=count+1
        Total=Total+int(data_row[1])
        if first:
            last_profit_loss=int(data_row[1])
            first=False
        else:
            change=int(data_row[1])-last_profit_loss
            Total_Change=Total_Change+change
            if change<Min_change:
                Min_change=change
                Date_of_Min=(data_row[0])
            if change>Max_change:
                Max_change=change
                Date_of_Max=(data_row[0])
            last_profit_loss=int(data_row[1])


#Print & Save Final Values with Formating 
lines = ["Financial Analysis",
        "----------------",
        f"Total Months:{count}",
        f"Total:$ {Total}",
        f"Average Change: $ {Total_Change/(count-1):.2f}",
        f"Greatest Increase In Profit: {Date_of_Max}  ( $ {Max_change})",
        f"Greatest Decrease in Profit: {Date_of_Min}  ( $ {Min_change})"
        ]
print(*lines, sep="\n")
with open("analysis/analysis.txt","wt") as f:
    print(*lines, sep="\n", file=f)
