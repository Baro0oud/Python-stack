# Change the value 10 in x to 15
x[1][0] = 15

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'

# Change the value 20 in z to 30
z[0]['y'] = 30

# Print the updated variables to verify changes
print("Updated x:", x)
print("Updated students:", students)
print("Updated sports_directory:", sports_directory)
print("Updated z:", z)

def iterateDictionary(some_list):
    for dictionary in some_list:
        output = ""
        for key, value in dictionary.items():
            output += f"{key} - {value}, "
        print(output[:-2])  # Remove the trailing comma and space


# Example list of dictionaries
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

# Call the function with the list of dictionaries
iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])


# Example list of dictionaries
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

# Call the function with different key names
print("First Names:")
iterateDictionary2('first_name', students)
print("\nLast Names:")
iterateDictionary2('last_name', students)

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(len(value), key.upper())
        for item in value:
            print(item)
        print()


# Example dictionary with lists as values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# Call the function with the dictionary
printInfo(dojo)
