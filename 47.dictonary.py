#dict
d1 = {102: 'rahul', 105: 'payal', 106: 'arjun', 107: 'prachi'} #dict is a collection of key value pairs. It is unordered, mutable and indexed. It is defined by using curly braces {}. Each key value pair is separated by a comma. The key and value are separated by a colon. The keys must be unique and immutable. The values can be of any data type.

print(d1) #prints the dict d1

print(d1[102],d1[105],d1[106],d1[107])#prints the values of the keys 102, 105, 106 and 107 in dict d1

for k in d1: #prints the keys in dict d1
     print(k) # prints the key k in dict d1

for k in d1: #prints the key value pairs in dict d1
     print(k, d1[k]) #prints the key k and its corresponding value d1[k] in dict d1

for k in d1: #prints the values of the keys in dict d1
     print(d1[k]) #prints the value of the key k in dict d1

i = 0 #prints the first two key value pairs in dict d1
for k in d1: #iterates through the keys in dict d1
    if i < 2: # checks if the value of i is less than 2
        print(k, d1[k]) #prints the key k and its corresponding value d1[k] in dict d1
        i += 1 #increments the value of i by 1
