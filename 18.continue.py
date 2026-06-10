i = 1 # Initialize a variable i to 1

while i <=10: # Start a while loop that will run as long as i is less than or equal to 10
    x = int(input("Enter a number: ")) # Inside the loop, take input from the user and store it in variable x as an integer

    if x %2==0: # Check if x is even
        continue # If x is even, skip the rest of the loop and go to the next iteration
    print(i,"x=",x) # If x is odd, print the value of i and x
    i+=1 # Increment i by 1 at the end of each iteration of the loop