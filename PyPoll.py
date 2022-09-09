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
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    first_row = next(file_reader)
    print(first_row)