# Import the datetime class from the datetime module.
import datetime as dt
from distutils import text_file
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
file_to_load = 'Resources/election_results.csv'
election_data = open(file_to_load, 'r')
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    #To do:read and analyze the data here
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)
     # Print each row in the CSV file.
    for row in file_reader:
        print(row)
         # Print the header row.
    headers = next(file_reader)
    print(headers)

    #Print the file object.
    print(election_data)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World,")
outfile.close()
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    txt_file.write("Hello World,\n ")
    outfile.close()
    # Write three counties to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("Arapahoe,\n ")
    txt_file.write("Denver,\n ")
    txt_file.write("Jefferson,\n ")






