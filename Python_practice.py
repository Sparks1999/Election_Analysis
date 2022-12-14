# counties = ["Arapahoe", "Denver", "Jefferson"]
# if counties[1] == "Denver":
#     print(counties[1])
# else:
#     print("Not Present")

# counties_2 = ["Arapahoe", "Denver", "Jefferson"]
# if "El Paso" in counties_2:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# if "Arapahoe" and "El Paso" in counties_2:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")

# if "Arapahoe" or "El Paso" in counties_2:
#     print("Arapahoe or El Paso are in the list of counties.")
# else:
#     print("Arapahoe and El Paso is not in the list of counties.")

# if "Arapahoe" in counties and "El Paso" not in counties:
#    print("Only Arapahoe is in the list of counties.")
# else:
#     print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# for county in counties_2:
#     print(county)

# for num in range(5):
#     print(num)

# for i in range(len(counties_2)):
#     print(counties_2[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county in counties_dict:
#     print(county)

# for county in counties_dict.keys():
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

# for county, voters in counties_dict.items():
#     print(county, voters)

# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

# for i in range(len(voting_data)):
#     print(voting_data[i]['county'])

# for country_dict in voting_data:
#     for value in country_dict.values():
#         print(value)

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# for county, voters in counties_dict.items():
#     print(f"{county} has {voters} registered voters.")

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# print(message_to_candidate)

for county, voters in counties_dict.items():
    print(f'{county} county has {voters} registered')

for county_dict in voting_data:
    print(f'{county_dict["county"]} county has {county_dict["registered_voters"]} registered voters.')

