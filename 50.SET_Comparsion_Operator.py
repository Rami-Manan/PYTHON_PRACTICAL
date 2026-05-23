s1 = {3,4,6,7,9,8} # set is unordered collection of unique elements
s2 = {3,4,6,5,9,7} # set is unordered collection of unique elements

if s1 == s2: 
    print("s1 and s2 are equal") 
elif s1 != s2:
    print("s1 and s2 are not equal")
elif s1 > s2:
    print("s1 is greater than s2")  
elif s1 < s2:
    print("s1 is less than s2")
elif s1 >= s2:
    print("s1 is greater than or equal to s2")
elif s1 <= s2:
    print("s1 is less than or equal to s2")

else:
    print("s1 and s2 are not comparable")