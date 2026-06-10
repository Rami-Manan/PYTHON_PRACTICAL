def function(x): # This function checks if x is greater than or equal to 3
    if x >= 3: # If x is greater than or equal to 3
        return x # Return x if it is greater than or equal to 3
    
y = [1, 2, 3, 4, 5] # This is a list of numbers from 1 to 5
l1 = list(filter(function, y)) # This applies the filter function to the list y and returns a new list l1 with only the elements that satisfy the condition in the function
print(l1) # This prints the list l1, which contains the elements from y that are greater than or equal to 3