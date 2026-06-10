l1 = [1,2,3] # Create a list l1 with the elements 1, 2, and 3
l2 = [2,3,1] # Create a list l2 with the elements 2, 3, and 1
l3 = [1,2,3,4,5] # Create a list l3 with the elements 1, 2, 3, 4, and 5
l4 = [1,2,3] # Create a list l4 with the elements 1, 2, and 3

if l1 == l2: # Compare the list l1 with the list l2 using the equality operator (==) to check if they are equal
    print("l1 and l2 are equal") # this will not be printed because the order of the elements in the list l1 and l2 is different
elif l1 == l3: # Compare the list l1 with the list l3 using the equality operator (==) to check if they are equal
    print("l1 and l3 are equal") # this will not be printed because the lists have different lengths
elif l1 == l4: # Compare the list l1 with the list l4 using the equality operator (==) to check if they are equal
    print("l1 and l4 are equal") # this will be printed because the lists are identical 
else: # If none of the above conditions are true, execute the code in this block
    print("l1 is not same to anyone") # this will be printed because the order of the elements in the list l1 and l2 is different and the lists l1 and l3 have different lengths.   
    