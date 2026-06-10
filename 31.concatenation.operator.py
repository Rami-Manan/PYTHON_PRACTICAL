l1 = [1,5,9] # Create a list l1 with the elements 1, 5, and 9
l2 = [2,3,1] # Create a list l2 with the elements 2, 3, and 1
l3 = l1 + l2  # Concatenation of two lists
print(l3) # Print the concatenated list l3 to the console, which should contain the elements 1, 5, 9, 2, 3, and 1 in that order.

l1+= l2  # l1 = l1+l2 # In-place concatenation of two lists
print(l1) # Print the modified list l1 to the console, which should now contain the elements 1, 5, 9, 2, 3, and 1 in that order after the in-place concatenation.
