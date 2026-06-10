def f1(*t):#a function f1 is defined that takes a variable number of arguments and stores them in a tuple t
    print(len(t))#the length of the tuple t is printed

f1(1, 2, 3)#the function f1 is called with three arguments, and it will print the length of the tuple, which is 3
f1(1, 2, 3, 4, 5)#the function f1 is called with five arguments, and it will print the length of the tuple, which is 5
f1(1, 2, 3, 4, 5, 6, 7, 8, 9)#the function f1 is called with nine arguments, and it will print the length of the tuple, which is 9