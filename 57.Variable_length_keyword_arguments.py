def personinfo(**kwargs): # this function takes variable length keyword arguments and prints them in the format of key : value.
    for k , v in kwargs.items(): # this loop iterates through the keyword arguments and prints them in the format of key : value.
        print(f"{k} : {v}") # this will print the key and value of the keyword arguments in the format of key : value.

personinfo(name = "Sameer", age = 22,) # this will print the name and age of the person because the function personinfo takes variable length keyword arguments and prints them in the format of key : value.
personinfo(name = "Ajay", age = 25, marks = 57)# this will print the name, age and marks of the person because the function personinfo takes variable length keyword arguments and prints them in the format of key : value.
personinfo(name = "Rahul", empid = 123, age =25) # this will print the name, empid and age of the person because the function personinfo takes variable length keyword arguments and prints them in the format of key : value.