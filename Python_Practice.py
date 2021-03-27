print("___________________")
print("___________________")

#voting_data = []

#voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
#voting_data.append({"county":"Denver", "registered_voters": 463353})
#voting_data.append({"county":"Jefferson", "registered_voters": 432438})

#print(voting_data)
#print("___________________")

#voting_data.insert(0, {"county":"El Paso", "registered_voters": 461149 })
#voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
#voting_data.pop(1)
#voting_data.append({'county': 'Denver', 'registered_voters': 463353})
#voting_data.append({"county":"Arapahoe", "registered_voters": 422829})

#print(voting_data)

#counties = ["Arapahoe", "Denver", "Jefferson"]
#if "El Paso" in counties:
#    print("El Pase is in the list of counties.")
#else:
#    print("El Paso is not in the list of counties")


#x=0
#while x<=5:
#    print(x)
#    x=x+11


#for county in counties:
#    print(county)


#print("___________________")
#print("___________________")



#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county in counties_dict.items():
#    print(county)

#for county in counties_dict:
#    print(counties_dict.get(county))

#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters.")

#adding commas to the voter numbers
#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters:,} registered voters.")

#print("___________________")
#print("___________________")



#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                {"county":"Denver", "registered_voters": 463353},
#                {"county":"Jefferson", "registered_voters": 432438}]

#for i in range(len(voting_data)):
#    print(voting_data[i])

#print("___________________")
#print("___________________")

#for x in voting_data:
#    for value in x.values():
#        print(value)

#print("___________________")
#print("___________________")

#for county_dict in voting_data:  

#     print(county_dict['registered_voters'])


#print("___________________")
#print("___________________")

#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))

#message_to_candidate = (
#    f"You received {candidate_votes:,} votes. "
#    f"The total number of votes in the election was {total_votes:,}. "
#    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#print(message_to_candidate)

#print("___________________")
#print("___________________")

#printing the values of speific keys in a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
         print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")

#print("___________________")
#print("___________________")

