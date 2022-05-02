# Election_Analysis
Election Analysis Project
## Project Overview
A Colorado Board of Elections employee has tasked me to complete an election audit of a recent local congressional election. They requested to have the total votes in the election broken down by candidate to determine the popular vote, and winning percentage. They then wanted to have a breakdown of the votes based on the vote counts in the county to determine which county had the highest turnout and percentage of votes.
#Purpose
Calculate the total number of votes cast for candidates, and to breakdown the turnout amount for each county.
Get a complete list of candidates who received votes.
Calculate the percentage of votes each candidate won.
Calculate the percentage of votes each candididate won.
Determine the winnder of the election based on the overall votes.
Calculate the amount of votes for each county and determine which county had the highest voter turnout.

##Resources
-Data Source: election_results.csv
-Software: Python 3.7.6, Visual Studio version 1.66.2
##Election Audit Results
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

I created a script to identify the unique candidate names,and calculate the number of votes each of those candidates received. Once the vote counts were received for each candidate, I was able to write script to calculate the percentage of votes each candidate received, in order to find the winner based on percentage and popular vote. This same script can be used in future elections. This scipt can be used for future elections by modifying the csv file path to pull the file, and making any changes to the script if there are any additional rows added. The modified script would include the new row index for the county and for the candidate, so that information can be updated with the new file information.
<img width="715" alt="Py_Poll_Challenge_Terminal Image" src="https://user-images.githubusercontent.com/99056132/166170500-df5af80e-6668-4700-94af-b464205a9e7c.png">
