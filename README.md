### Election_Analysis

## Project Overview
A Colorado Board of Elections employee has tasked me to complete an election audit of a recent local congressional election. They requested to have the total votes in the election broken down by candidate to determine the popular vote, and winning percentage. They then wanted to have a breakdown of the votes based on the vote counts in the county to determine which county had the highest turnout and percentage of votes.
##**Purpose**
Calculate the total number of votes cast for candidates, and to breakdown the turnout amount for each county.
Get a complete list of candidates who received votes.
Calculate the percentage of votes each candidate won.
Calculate the percentage of votes each candididate won.
Determine the winnder of the election based on the overall votes.
Calculate the amount of votes for each county and determine which county had the highest voter turnout.

##**Resources**
-Data Source: election_results.csv
-Software: Python 3.7.6, Visual Studio version 1.66.2
##**Election Audit Results**
The analysis of the election_results_csv shows that there were a total of 369,711 votes cast in the election.
There were 3 candidates in the election. 
-Candidate 1 was Charles Casper Stockham.
-Candidate 2 was Diana DeGette.
-Candidate 3 was Raymon Anthony Doane.
-Candidate 1 received 23.0% of the votes and 85,213 total votes.
-Candidate 2 received 73.8% of the votes and 272,892 total votes.
-Candidate 3 received 3.1% of the votes and  11,606 total votes.
-The winner of the election was Candidate 2, who received 73.8% of the vote and 272,892 total votes. 
-The winning county is Denver, who received 82.8% of the votes for a total of 306,055 votes.

<img width="715" alt="Py_Poll_Challenge_Terminal Image" src="https://user-images.githubusercontent.com/99056132/166170500-df5af80e-6668-4700-94af-b464205a9e7c.png">
##**Election Audit Summary**
I created a script to identify the unique candidate names,and calculate the number of votes each of those candidates received. Once the vote counts were received for each candidate, I was able to write script to calculate the percentage of votes each candidate received, in order to find the winner based on percentage and popular vote. This same script can be used in future elections. This scipt can be used for future elections by modifying the csv file path to pull the file, and making any changes to the script if there are any additional rows added. The modified script would include the new row index for the county and for the candidate, so that information can be updated with the new file information.

#Script Used for Audit
# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}


# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
winning_countycount = 0
count_highestturnout = ""


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes += 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        
        county_name = row[1]
        

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
       
        if county_name not in county_options:
            

            # 4b: Add the existing county to the list of counties.
            
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
        
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.

        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.

    for county_name in county_options:
        

        # 6b: Retrieve the county vote count.
        votes = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

         # 6d: Print the county results to the terminal.
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > winning_countycount):
            winning_countycount = votes
            count_highestturnout = county_name

    # 7: Print the county with the largest turnout to the terminal.
    # Print the winning candidate's results to the terminal.
    winning_county_summary = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {count_highestturnout}\n"
        f"-------------------------\n")
    print(winning_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

