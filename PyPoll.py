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

#open the file as a file object
with open(file_to_load) as election_data:

    #Assign file object to a variable and read to it
    file_reader = csv.reader(election_data)

    #print each rowin the CSV file.
    #for row in file_reader:
    #    print(row)
    
    #print header row
    headers = next(file_reader)
    print(headers)



#using open() function with "w" mode to write data to the save file
#using "with" to open the save file as a text file
#with open(file_to_save, "w") as txt_file:

##outfile = open(file_to_save, "w")
#    txt_file.write("Counties in the Election\n")
#    txt_file.write("-------------------------\n")
#    txt_file.write("Arapahoe\n")
#    txt_file.write("Denver\n")    
#    txt_file.write("Jefferson")

#"close" command not needed when "with" is used. 
##outfile.close()


#   To do: perform analysis
#    print(election_data)

