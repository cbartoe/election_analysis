#Goals Of The Project
#1. Total number of votes cast
#2. A complete list of candidates who received votes
#3. Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular vote

#PseudoCode
#1. open the data file
#2. write down names of candidates 
#3. add vote count for each candidate
#3. calculate total votes per candidate
#4. calculate total votes cast in election
#5. calculate percentages of canditate/total
#6. print outputs and name winner

print("-----------------------------------\n")

#import dependencies
import csv
import os

#INPUT Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")

#OUTPUT create and assign a save file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file
##election_data = open(file_to_load, "r"):
    #MUST have 'election_data.close()' at the end**

#Initialize total voter counter
total_votes = 0

#initiialize candidate name list
candidate_options = []

#create candidate_votes dictionary
candidate_votes = {}

#initialize winning_candidate
winning_candidate = ""

#initialize winning count
winning_count = 0

#initialize winning percentage
winning_percentage = 0 

#open the file as a file object
with open(file_to_load) as election_data:

    #Assign file object to a variable and read to it
    file_reader = csv.reader(election_data)

    #print each rowin the CSV file.
    #for row in file_reader:
    #    print(row)
    
    #print header row
    headers = next(file_reader)
   
    #print each row of the csv file
    for row in file_reader:
        total_votes += 1

        #print the candidate's name from each row
        candidate_name = row[2]

        #eliminating duplidcates
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #begin tracking votes
            candidate_votes[candidate_name] = 0 

        #increment candidate vote
        candidate_votes[candidate_name] += 1

    #Save results to text file
    with open(file_to_save, "w") as txt_file:

        election_results = (
            f"\nElection Results\n"
            f"--------------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"--------------------------------\n")
        print(election_results, end="")
        txt_file.write(election_results)

        #calculate vote percentages
        for candidate_name in candidate_votes: 
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes) / float(total_votes) * 100

            #print percent outcomes
            #print(f"{candidate_name}: {vote_percentage:.1f}% ({candidate_votes[candidate_name]})\n")
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({candidate_votes[candidate_name]})\n")

            #print candidate results and save to the election_analysis.txt file
            print(candidate_results)
            txt_file.write(candidate_results)

            #determine winning candidate
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes 
                winning_percentage = vote_percentage
                winning_candidate = candidate_name

        winning_candidate_summary = (f"-----------------------------------\n"
                                    f"Winner: {winning_candidate}\n"
                                    f"Winning Vote Count: {winning_count:,}\n"
                                    f"Winning Percentage: {winning_percentage:.1f}%\n"
                                    f"-----------------------------------\n")
        #print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
        
