s1 = {3,4,6,7,9,8} # set is unordered collection of unique elements
s2 = {3,4,6,5,9,7} # set is unordered collection of unique elements

if s1 == s2:  # if s1 and s2 have the same elements, regardless of order, they are considered equal
    print("s1 and s2 are equal")  # if s1 and s2 have the same elements, regardless of order, they are considered equal
elif s1 != s2: # if s1 and s2 do not have the same elements, they are considered not equal
    print("s1 and s2 are not equal") # if s1 and s2 do not have the same elements, they are considered not equal
elif s1 > s2: # if s1 has all the elements of s2 and at least one additional element, then s1 is considered greater than s2
    print("s1 is greater than s2")  # if s1 has all the elements of s2 and at least one additional element, then s1 is considered greater than s2
elif s1 < s2: # if s1 has all the elements of s2 and at least one additional element, then s1 is considered less than s2
    print("s1 is less than s2") # if s1 has all the elements of s2 and at least one additional element, then s1 is considered less than s2
elif s1 >= s2: # if s1 has all the elements of s2 (s1 is a superset of s2), then s1 is considered greater than or equal to s2
    print("s1 is greater than or equal to s2") # if s1 has all the elements of s2 (s1 is a superset of s2), then s1 is considered greater than or equal to s2
elif s1 <= s2: # if s1 has all the elements of s2 (s1 is a subset of s2), then s1 is considered less than or equal to s2
    print("s1 is less than or equal to s2") # if s1 has all the elements of s2 (s1 is a subset of s2), then s1 is considered less than or equal to s2

else: # if none of the above conditions are met, it means that s1 and s2 are not comparable in terms of their elements, and we can print a message indicating that they are not comparable.
    print("s1 and s2 are not comparable") # if none of the above conditions are met, it means that s1 and s2 are not comparable in terms of their elements, and we can print a message indicating that they are not comparable.