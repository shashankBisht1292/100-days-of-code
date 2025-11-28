#Dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Function"])

programming_dictionary["Loop"] = "The action of doing something again and again."

print(programming_dictionary)

empty_dictionary = {}

#wipe the existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

#loop through the dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Nesting a List inside a Dictionary
capitals = {
    'France': 'Paris',
    'Germany': 'Berlin',
}

#Nested List in Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }

# print lille
# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
#print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visited": 8,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visited": 5,
    },
}

print(travel_log["Germany"]["cities_visited"][2])