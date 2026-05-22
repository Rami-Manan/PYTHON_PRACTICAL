l1 = [1,2,3]
l2 = [2,3,1]
l3 = [1,2,3,4,5]
l4 = [1,2,3]

if l1 == l2:
    print("l1 and l2 are equal") # this will not be printed because the order of the elements in the list l1 and l2 is different
elif l1 == l3:
    print("l1 and l3 are equal") # this will not be printed because the lists have different lengths
elif l1 == l4:
    print("l1 and l4 are equal") # this will be printed because the lists are identical 
else:
    print("l1 is not same to anyone") # this will be printed because the order of the elements in the list l1 and l2 is different and the lists l1 and l3 have different lengths.   
    