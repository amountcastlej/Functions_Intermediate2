#1 Update Values in Dictionaries and Lists
# x = [ [5,2,3], [10,8,9] ] 
# x[1][0] = 15
# print(x)

# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# students[0]['last_name'] = ['Bryant']
# print(students[0]['last_name'])

# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# sports_directory['soccer'][0] = ['Andres']
# print(sports_directory['soccer'][0])

# z = [ {'x': 10, 'y': 20} ]
# z[0]['y'] = 30
# print(z[0]['y'])

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

#2 Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key and the associated value. 
# For example, given the following list:

# def iterateDictionary(some_list):
#     for idx in range(len(some_list)): # Loops through list of dictionaries
#         student_dict = some_list[idx]
#         for key in some_list[idx]: # loops through keys inside of dictionary
#             print(key, '-', student_dict[key])
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# iterateDictionary(students)

def list_of_gum(kind_of_gum):
    for x in range(len(kind_of_gum)):
        for thing in kind_of_gum[x]:
            print(thing, kind_of_gum[x][thing])
gums = [
    {'make': 'sugary', 'model': 'Winterfresh'},
    {'make': 'sugarfree', 'model': 'Trident'},
    {'make': 'bubblegum', 'model': 'BubbleYum'}
]
# list_of_gum(gums)

def iterateDictionary(key_val, some_list):
    for x in range(len(some_list)):
        for comp in some_list[x]:
            print(comp, some_list[x][comp])
computers = [
    {'make': 'Dell', 'model': 'XPS'},
    {'make': 'Windows', 'model': '10'},
    {'make': 'Apple', 'model': 'Macbook'}
]
# iterateDictionary('make', computers)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#3 Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
# the function prints the value stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB
# def iterateDictionary2(key_name, some_list):
#     for idx in range(len(some_list)):
#         print(some_list[idx][key_name])
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
def iterateDictionary2(key_name, some_list):
    for x in range(len(some_list)):
        print(some_list[x][key_name])
cars = [
    {'make': 'BMW', 'model': 'M3'},
    {'make': 'Porsche', 'model': '911'},
    {'make': 'Subaru', 'model': 'WRX'}, 
    {'make': 'Toyota', 'model': 'Corolla'}
]
# iterateDictionary2(cars)
# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)
# And iterateDictionary2('last_name', students) should output:

# Jordan
# Rosales
# Guillen
# Tonel

# 4. Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, 
# and then prints the associated values within each key's list. For example:

# def printInfo(some_dict):
#     for key in some_dict:
#         print(len(some_dict[key]), key.upper())
#         for val in some_dict[key]:
#             print(val)

def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]))
        for val in some_dict[key]:
            print(val)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# printInfo(dojo)

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

def iterateDictionary(some_list):
    for i in range(len(some_list)):
        for thing in some_list[i]:
            print(thing, some_list[i][thing])
soda = [
    {'brand': 'coke', 'color': 'brown'},
    {'brand': 'sprite', 'color': 'clear'},
    {'brand': 'mountaindew', 'color': 'yellow'}
]
# iterateDictionary(soda)

def iterateDictionary(some_list):
    for x in range(len(some_list)):
        for thing in some_list[x]:
            print(thing, some_list[x][thing])
cats = [
    {'hair': 'long', 'color': 'orange'},
    {'hair': 'medium', 'color': 'black'},
    {'hair': 'short', 'color': 'white'}
]
iterateDictionary(cats)