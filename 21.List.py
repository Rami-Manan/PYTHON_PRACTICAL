l1 = [50,20,30,10,40] # Create a list l1 with the elements 50, 20, 30, 10, and 40

# Unpack the list l1 into three variables: first, all, and last. The first variable will take the first element of the list, the last variable will take the last element of the list, and the all variable will take all the elements in between as a list.
first, *all, last = l1 
print(first) # Print the first element of the list
print(all) # Print all elements except the first and last
print(last) # Print the last element of the list