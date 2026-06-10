#function is a block of code which performs a specific task. It is reusable and can be called multiple times in a program. It helps in breaking down a large program into smaller and manageable parts.
def f1(): #function definition
    a = int(input("Enter a number: ")) #takes input from user and converts it to integer
    b = a ** 2 #calculates the square of a and stores it in b
    print("square of", a, "is", b) #prints the square of a

f1()#calls the function f1 to execute the code inside it