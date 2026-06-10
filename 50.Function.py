# takes nothing, returns nothing


def add_no_args(): # This function is defined to take no arguments and return nothing. It will prompt the user to enter two numbers, read the input, convert it to integers, add them together, and print the result.
    print("Enter two numbers: ") # This line prints a message to the user asking them to enter two numbers.
    a = int(input()) # This line reads the input from the user, converts it to an integer, and stores it in the variable a.
    b = int(input()) # This line reads the input from the user, converts it to an integer, and stores it in the variable b.
    c = a + b # This line adds the two numbers a and b together and stores the result in the variable c.
    print("Sum is", c) # This line prints the message "Sum is" followed by the value of c, which is the sum of a and b.


add_no_args() # This line calls the function add_no_args, which will execute the code inside the function and perform the task of adding two numbers entered by the user and printing the result.
