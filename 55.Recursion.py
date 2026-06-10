#loop 
'''def f1():
    print("Hello")#the function f1 prints "Hello"
    f1()#the function calls itself

f1()#the function f1 is called, and it will print "Hello" / infinitely until a maximum recursion depth error occurs''' 

def f1(n):#a function f1 is defined that takes a parameter n
    i = 1#the variable i is initialized to 1
    while i<=n:#a while loop is used to iterate as long as i is less
        print("Hello")#the function prints "Hello"
        i+=1#the variable i is incremented by 1 
f1(3)#the function f1 is called with the argument 3, and it will print "Hello" three times