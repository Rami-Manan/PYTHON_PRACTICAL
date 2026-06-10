t1 = (10,5,20,15) # Create a tuple t1 with the elements 10, 5, 20, and 15
print(t1[0]) # Print the first element of the tuple t1
print(t1[1]) # Print the second element of the tuple t1
print(t1[2]) # Print the third element of the tuple t1
print(t1[3]) # Print the fourth element of the tuple t1
print("\n")

a=len(t1) # Calculate the length of the tuple t1 and store it in the variable a
print(a) # Print the length of the tuple t1 to the console, which should be 4 since there are four elements in the tuple.

i=0 # Initialize a variable i to 0, which will be used as an index to access the elements of the tuple t1 in a while loop.
while i < len(t1): # Start a while loop that will run as long as i is less than the length of the tuple t1 (which is 4 in this case).
    print(t1[i]) # Inside the loop, print the element at index i of the tuple t1 to the console. This will print each element of the tuple one by one as the loop iterates through it.
    i+=1 # Increment i by 1 at the end of each iteration of the loop to move to the next index in the tuple t1, allowing the loop to access and print the next element in the tuple during the next iteration.
print("\n")

for i in t1: # Start a for loop that iterates over each element in the tuple t1, assigning the current element to the variable i during each iteration of the loop. This allows us to access and print each element of the tuple directly without needing to use an index.
    print(i) # Inside the loop, print the current element (i) being iterated over to the console. This will print each element of the tuple t1 one by one as the loop iterates through it.

