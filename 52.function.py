# takes something, returns something

def add_return_value(a, b): # This function is defined to take two arguments a and b, and return the sum of a and b. It will prompt the user to enter two numbers, read the input, convert it to integers, add them together, and return the result.
    print("Enter two numbers: ") # This line prints a message to the user asking them to enter two numbers.
    a = int(input()) # This line reads the input from the user, converts it to an integer, and stores it in the variable a.
    b = int(input()) # This line reads the input from the user, converts it to an integer, and stores it in the variable b.
    d = a + b # This line adds the two numbers a and b together and stores the result in the variable d.
    return d # This line returns the value of d, which is the sum of a and b, to the caller of the function. 


s = add_return_value(0, 0) # This line calls the function add_return_value with the arguments 0 and 0. The function will execute the code inside it, prompt the user to enter two numbers, read the input, convert it to integers, add them together, and return the result. The returned value will be stored in the variable s.
print("Sum is", s) # This line prints the message "Sum is" followed by the value of s, which is the sum of the two numbers entered by the user and returned by the function add_return_value.