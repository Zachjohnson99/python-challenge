import os
import csv
from pathlib import Path 

# assign file location with the pathlib library
csv_file_path = "hw3-election_data.csv"

# variables and set to 0
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#now open the file in csvreader
with open(csv_file_path, newline="") as elections:

    # sore data under the csvreader variable
    csvreader = csv.reader(elections, delimiter=",") 

    #skip the header so we iterate through the actual values
    header = next(csvreader)     

    # iterate through each row in the csv
    for row in csvreader: 

        #count the unique Voter ID's and store in variable  called total_votes
        total_votes +=1

        #using +=1 to essetianlly add 1 everytime a vote is for that particular canidate
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, otooley_votes]

 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key = dict_candidates_and_votes.get)

# print a the summary of the analysis
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

#print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

#asign output file location
output_file = "Election_Results_Summary.txt"

with open(output_file,"w") as file:

# write to output file 
    file.write(f"Election Results")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")