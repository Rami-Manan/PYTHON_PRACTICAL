x = int(input("Enter a number: ")) # Take input from the user and store it in variable x as an integer
y = int(input("Enter another number: " )) # Take input from the user and store it in variable y as an integer
z = int(input("Enter a third number :")) # Take input from the user and store it in variable z as an integer

if x%2==0 and y%2==0 and z%2==0: # Check if x, y, and z are all even numbers
    print("you win")        # If all three numbers are even, print "you win"
else: # If any of the numbers is not even, print "game over"
    print("game over") # If any of the numbers is not even, print "game over"