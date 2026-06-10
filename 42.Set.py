s1 = {1, 5, 8} # set of integers.
s2 = {10, 2, 8, 1, 11,8} # set of integers with duplicate values (8 is repeated)
s3 =  {} # this creates an empty dictionary, not a set. To create an empty set, use set() instead.
s4 = set() # this creates an empty set. It is the correct way to create an empty set in Python.
s5 = set([1, 2, 3, 4, 5]) # this creates a set from a list of integers. The set will contain the unique elements from the list.

for i in s1: # iterating through the set s1 and printing each element
    print(i) # prints each element in the set s1 on a new line
    
    

for i in s2: # iterating through the set s2 and printing each element
    print(i) # prints each element in the set s2 on a new line
    print("\n")

for i in s3: # iterating through the set s3 and printing each element
    print(i) # prints each element in the set s3 on a new line

for i in s4: # iterating through the set s4 and printing each element
    print(i) # prints each element in the set s4 on a new line
    
for i in s5: # iterating through the set s5 and printing each element
    print(i) # prints each element in the set s5 on a new line
