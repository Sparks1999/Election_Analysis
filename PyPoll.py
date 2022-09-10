# Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
# election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
# election_data.close()

# with open(file_to_load) as election_data:
#     print(election_data)

#Import modules
# import csv
# import os
# #Add filename variable
# file_to_load = os.path.join("Resources", "election_results.csv")
# #Open file
# with open(file_to_load) as election_data:
      
#     #Print the file object
#     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# outfile = open(file_to_save, "w")
# #Write some data to the file
# outfile.write("Hello World")

# outfile.close

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file.
#     txt_file.write("Hello World\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")
 
# Add our dependencies.
import csv
from functools import total_ordering
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Set total votes count to 0
total_votes = 0

#Declareing a new list for candidates names
candidate_options = []

#Creating a dict for number of votes a candidate has
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)
       
        #Add total vote count
        total_votes += 1
       
        #Print candidate names for each row
        candidate_names = row[2]

        #Code to check if a candidate was already in the candidate_options list
        if candidate_names not in candidate_options:
        
        #Add candidates names to candidates_options list
            candidate_options.append(candidate_names)

            #Begin tracking candidates votes (creating keys for the dict)
            candidate_votes[candidate_names] = 0

        #Adding one tally each time a candidate shows up
        candidate_votes[candidate_names] += 1

    with open(file_to_save, "w") as txt_file:
    
        #Printing results to a text file
        election_results = (
            f"Election Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        #Calculating the percentage of votes each candidate has
        for candidate_name in candidate_votes:

            #Retrive vote count from the candidates_vote dict
            votes = candidate_votes[candidate_name]

            #Calculate percentage
            vote_percent = float(votes)/ float(total_votes) * 100

            #print out each candidate's name, vote count, and percentage of votes to the terminal.
            # print(f"{candidate_name}: {vote_percent:.1f}% ({votes:,})\n")

            # Determine winning vote count and candidate
            # 1. Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percent > winning_percentage):
                # 2. If true then set winning_count = votes and winning_percent = vote_percentage.
                winning_count = votes
                winning_percentage = vote_percent
                # 3. Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name

        #Print out the winning candidate and their percentage of votes
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        
        #Decling the variable candidates_results
        candidates_results = (f"{candidate_name}: {vote_percent:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidates_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidates_results)
