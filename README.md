# Election Analysis

## Project Overview
A Coloardo Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

**Goals Of The Project:**
  1. Calculate the total number of votes cast in the election
  2. Get a complete list of candidates who received votes
  3. Calculate the total number of votes each candidate received
  4. Calculate the percentage of votes each candidate recieved
  5. Determine the winner of the election based on popular vote
  6. Identify the countys included in the data set
  7. Calculate the number of votes per county
  8. Determine which county had the largest turnout

## Resources
  1. Data Source: election_results.csv
  2. Software: Python 3.9.1, Visual Studio Code 1.54.3

## Summary
The analysis of the election data shows that **369,711** total votes were cast between 3 candidates and across 3 counties.

**County Break Down:** 
  (From highest to lowest turnout rates)
  1. Denver: 82.8% (306,055)
  2. Jefferson: 10.5% (38,855)
  3. Arapahoe: 6.7% (24,801)
 
  **Largest County Turnout: Denver**
  
**Candidate Break Down:** 
  (From highest to lowest vote counts)
  1. **Diana DeGette:** 73.8% (272,892) 
  2. **Charles Casper Stockham:** 23.0% (85,213) 
  3. **Ryan Anthony Doane:** 3.1% (11,606)

  **The winner of the election was Diana Degette** by a landslide with 73.8% and 272,892 of the votes. 

### Coommand Line Output 
![Command Line Outcomes](https://github.com/ghynox/election_analysis/blob/main/command_line_output.png)

## Challenge Overview
The data was examined using a loop that would run once through the set of data and on each line observe the name of the candidate and county. If the county or candidate was not yet on their appropriate list, the code added the candidate and then began tally votes awarded. Once the counties and candidates were appropraitely added to their lists, the loop just finished counting the votes for each. 

![Counting For Loop](https://github.com/ghynox/election_analysis/blob/main/aggregation_for_loop.png)

After the tallies were finished, the code ran through each county and each member to determine what percentage of the votes each attained and  which of them had the highest number of votes.

![County Calcs](https://github.com/ghynox/election_analysis/blob/main/county_calculations.png)
![Candidate_Calcs](https://github.com/ghynox/election_analysis/blob/main/candidate_calculations.png)

## Challenge Summary
This code has great potential to be used in further elections to break down the vote counts and to determine the winners, regions of highest turnout, and even confirm that there were no duplicate ballots. Some modifications that could enhance this code with future rollouts would be to:
  1. Adding lines of code to organize the counties and candidates in a descending order based on number of votes so that it is easy to see at first glance who won and then who followed in succession. 
  2. This codde could also be modified to see which candidate performed best in each county. 
  3. If it were possible to collect more data regarding the exact polling station, time of ballot casting, or other demographics, this code could be modified to determine demographics of who supported which candidate, and even determine which dates and times had the highest turnouts in each county. 
