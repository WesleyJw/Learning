#%% [markdown]

## Efficient Python Basics

### Pythonic Constructors

#%%
names = ["jose", "maria", "joao", "rita", "josefa"]

# Create a new list with names with more than six words

# Nothing pythonic approach

i = 0
new_list = []

while i < len(names):
    if len(names[i]) < 6:
        new_list.append(names[i])
    i += 1

print("Nothing pythonic approach:", new_list)

# Better, close to pathonic approach

new_list = []
for name in names:
    if len(name) < 6:
        new_list.append(name)
        
print("Close to pathonic approach: ", new_list)

# Pythonic

new_list = [name for name in names if len(name) < 6]
print("Pythonic: ", new_list)

#%% [markdown]

### Building with built ins
# Above we will start with some built in python types, functions and modules.

#### Range()
# The range function create a range of values, but a pythonic way to work with this function is use '*'
# simbol to unpack into a list of values
# %% 
numbers = range(10)
print('Numbers:', numbers)

# how to convert the range to a list?
# No pythonic way
number_list = list(numbers)
print('List Numbers:', number_list)

# Pythonic
number_list2 = [*numbers]
print("Pythonic list numbers: ", number_list2)

# To be more directly, we can do:
print("Pthonic:", [*range(0,100, 10)])

# %% [markdown]

#### Enumerate

# The enumerate function create a index for each element in a list. To be more directly using enumerate
# we can get the index (position of element into a list) and the element name.

# %%
names = ["jose", "maria", "joao", "rita", "josefa"]

# now we can get the index and the name of each element into a list

# A non pythonic way to get index and name
indexed_names = []
for index, name in enumerate(names):
    print(index, ":", name)
    indexed_names.append((index, name))
print("Indexed names from list: ", indexed_names)

# Pythonic: for loop list using compreension
indexed_names_list_comp = [(i, name) for i, name in enumerate(names)]
print("For loop list compreension: ", indexed_names_list_comp)

# Really pythonic: unpack an enumarate object with a start index of one
# if you want that the index start with another number. replace 1 with the numer that you want.
indexed_names_list_unpack = [*enumerate(names, 1)]
print("Unpack: ", indexed_names_list_unpack)

# %% [markdown]

#### map

# With this function is possible apply a function to each element in an object

# To use this function we can pass to args, firt the function to be applied and second
# the element  

# %%
names = ["jose", "maria", "joao", "rita", "josefa"]

names_upp = map(str.upper, names)

print("Names upper: ", names_upp)

# As you can see there aren't names into object names_upp, because this is a map object

# We can print the type of the map_upp object

print("Type of names_upp: ", type(names_upp))

# to see all names, we can unpack names into a list
names_upp_list = [*names_upp]

print("List or names upp: ", names_upp_list)

# We can use map function with integer object too
number_list = [1.2, 1.5, 1.3, 1.5, 2]

round_number = map(round, number_list)

print("Round numbers: ", round_number)

print("List or names upp: ", [*round_number])

# map also can be used with lambda function to apply a function 
number_cubic = map(lambda x: x**3, number_list)

print("Cubic numbers: ", [*number_cubic])

# %% [markdown]

#### References

# This tutorial was made with Cassio Bolba post. 

# Use link to see all content: https://cassio-bolba.medium.com/efficient-python-part-1-start-with-the-basics-4b40b12a562f.
