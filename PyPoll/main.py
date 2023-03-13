#Import framework
import os
import csv

# Import from location
Election_csv = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

#Open and Read data
with open(Election_csv) as Election_file:
    file_reader = csv.reader(Election_file, delimiter=",")

    csv_header = next(Election_file)
  
    
#Variable Containers
    Total_Lines = 0
    Candidate_Data =  {}

#Looping Actions to build outputs for each candidates
    for data_row in file_reader:
        
        Candidate_Name = data_row[2] 
        Total_Lines=Total_Lines+1
        if Candidate_Name not in Candidate_Data:
            Candidate_Data[Candidate_Name]= 0
    
        Candidate_Data[Candidate_Name]=Candidate_Data[Candidate_Name]+1

       
# Find a Winner
Winner = None

for Candidate_Name in Candidate_Data:
    if Winner is None:
        Winner = Candidate_Name
    elif Candidate_Data[Candidate_Name] > Candidate_Data[Winner]:
        Winner=Candidate_Name
    
# Print, Export & Save Outputs with a specified data presentation structure
Output =    ["Election Results",
            "--------------------",
            f"Total Votes: {Total_Lines}",
            "--------------------"
            ]
for Candidate_Name in Candidate_Data:
    Output.append(f"{Candidate_Name}: {(Candidate_Data[Candidate_Name]/Total_Lines):.3%} ({Candidate_Data[Candidate_Name]})")
Output.extend([
            "--------------------",
            f"Winner: {Winner}",
            "--------------------"
            ])

print(*Output, sep="\n")
with open("analysis/analysis.txt","wt") as f:
    print(*Output, sep="\n", file=f)