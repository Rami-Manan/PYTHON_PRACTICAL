s1={1, 2, 3} # Create a set s1 with the elements 1, 2, and 3. Sets are unordered collections of unique elements, so s1 will contain these three integers without any particular order.
s2={1, 2, 3} # Create another set s2 with the same elements as s1. Since sets are unordered collections of unique elements, s2 will also contain the integers 1, 2, and 3 without any particular order. Even though s1 and s2 are created separately, they contain the same unique elements, so they will be considered equal when compared.

# if else statement
if s1==s2: # Check if s1 and s2 are equal, which means they contain the same unique elements regardless of their order. Since both s1 and s2 contain the integers 1, 2, and 3, this condition will evaluate to True.
    print("s1 and s2 are equal")
else:   # If the condition s1 == s2 is not true, this block will be executed. However, since s1 and s2 are equal, this else block will not be executed in this case.
    print("s1 and s2 are not equal")
if s1!=s2: # Check if s1 and s2 are not equal, which means they do not contain the same unique elements. Since both s1 and s2 contain the integers 1, 2, and 3, this condition will evaluate to False.
    print("s1 and s2 are not equal")    
else:   # If the condition s1 != s2 is not true, this block will be executed. Since s1 and s2 are equal, this else block will be executed, and it will print "s1 and s2 are equal". However, since we already printed "s1 and s2 are equal" in the previous if statement, this else block will not be executed in this case. 
    print("s1 and s2 are equal")
if s1<s2: # Check if s1 is less than s2, which means that s1 has all the elements of s2 and at least one additional element. Since s1 and s2 contain the same elements, this condition will evaluate to False.
    print("s1 is less than s2")
else:   # If the condition s1 < s2 is not true, this block will be executed. Since s1 and s2 are equal, this else block will be executed, and it will print "s1 is not less than s2".
    print("s1 is not less than s2")
if s1<=s2: # Check if s1 is less than or equal to s2, which means that s1 has all the elements of s2 (s1 is a subset of s2). Since s1 and s2 contain the same elements, this condition will evaluate to True.
    print("s1 is less than or equal to s2")
else:   # If the condition s1 <= s2 is not true, this block will be executed. However, since s1 and s2 are equal, this else block will not be executed in this case.
    print("s1 is not less than or equal to s2")
if s1>s2: # Check if s1 is greater than s2, which means that s1 has all the elements of s2 and at least one additional element. Since s1 and s2 contain the same elements, this condition will evaluate to False.
    print("s1 is greater than s2")
else:   # If the condition s1 > s2 is not true, this block will be executed. Since s1 and s2 are equal, this else block will be executed, and it will print "s1 is not greater than s2".
    print("s1 is not greater than s2")
if s1>=s2: # Check if s1 is greater than or equal to s2, which means that s1 has all the elements of s2 (s1 is a superset of s2). Since s1 and s2 contain the same elements, this condition will evaluate to True.
    print("s1 is greater than or equal to s2")
else:   # If the condition s1 >= s2 is not true, this block will be executed. However, since s1 and s2 are equal, this else block will not be executed in this case.
    print("s1 is not greater than or equal to s2")