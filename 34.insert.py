'''l1 = [50,20,80,10,60,40]

l1.insert(2,90) # here we are adding the value of 90 to the list l1 at index 2 and after this line we can use the list l1 because it is not deleted


l2 = [50,20,80,10,60,40]

l2.insert(-3,55) # here we are adding the value of 90 to the list l2 at index -3 and after this line we can use the list l2 because it is not deleted   

print(l1) # this will show the list l1 with the new value of 90 added to the list at index 2 and the output will be [50,20,90,80,10,60,40]
print(l2) # this will show the list l2 with the new value of 90 added to the list at index -3 and the output will be [50,20,80,90,10,60,40]
'''

l1 = [50,20,80,10,60,40]

del l1[2] # here we are deleting the value of 80 from the list l1 at index 2 and after this line we can use the list l1 because it is not deleted
l1[2] = 90 # here we are adding the value of 90 to the list l1 at index 2 and after this line we can use the list l1 because it is not deleted
l1.append(75) # here we are adding the value of 75 to the end of the list l1 and after this line we can use the list l1 because it is not deleted
l1.insert(5,70) # here we are adding the value of 70 to the list l1 at index 5 and after this line we can use the list l1 because it is not deleted

print(l1) # this will show the list l1 with the new value of 90 added to the list at index 2 and the value of 75 added to the end of the list and the value of 70 added to the list at index 5 and the output will be [50,20,90,10,60,70,40,75]

print(l1[2]) # this will show the value