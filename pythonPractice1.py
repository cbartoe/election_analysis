
#gather data
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("How many total votes in the election? "))

#calculate %
percentage_votes = (my_votes/total_votes) * 100

#print %
print(f"You achieved {percentage_votes}% of the total votes")

#win/lose decision statement
if percentage_votes > 50:
    print("You have won the election!")
else:
    print("Sorry, better luck next time.")
