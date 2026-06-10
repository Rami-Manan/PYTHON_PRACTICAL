x = int(input("Enter a number: ")) # Take input from the user and store it in variable x as an integer
y = int(input("Enter another number: " )) # Take input from the user and store it in variable y as an integer
z = int(input("Enter a third number :")) # Take input from the user and store it in variable z as an integer

if x%2==0: # Check if x is an even number
    print("x is even") # If x is even, print "x is even"
else: # If x is not even, print "x is odd"
    print("x is odd")   # If x is not even, print "x is odd" 
if y%2==0: # Check if y is an even number
    print("y is even")  # If y is even, print "y is even" 
else: # If y is not even, print "y is odd"
    print("y is odd") # If y is not even, print "y is odd"
if z%2==0: # Check if z is an even number
    print("z is even") # If z is even, print "z is even"
else:     # If z is not even, print "z is odd"
    print("z is odd") # If z is not even, print "z is odd"

if x%2==0 and y%2==0 and z%2==0: # Check if x, y, and z are all even numbers
    print("you win")        # If all three numbers are even, print "you win"
else: # If any of the numbers is not even, print "game over"
    print("game over") # If any of the numbers is not even, print "game over"