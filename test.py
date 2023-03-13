import os
import csv

cereal_csv = os.path.join("..","PyBank", "PyBank", "Resources", "budget_data.csv")
print(cereal_csv)


with open(cereal_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    # csv_row2 = next(csv_file)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csv_reader:
        print(row)
   