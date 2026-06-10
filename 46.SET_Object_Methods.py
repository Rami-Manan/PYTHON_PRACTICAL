# Set object methods — each section shows one method and its result

s1 = {3, 4, 6, 7, 8, 9}  # unordered collection of unique elements
s2 = {7, 8, 50}          # second set (50 is only in s2 — useful for union / intersection)

print("Original s1:", s1)
print()

# --- add: insert one element ---
s1.add(10) # Add the element 10 to the set s1. If 10 is not already in s1, it will be added; if it is already present, s1 will remain unchanged since sets do not allow duplicate elements.
print("add(10)     ->", s1)

# --- remove: delete element (raises KeyError if missing) ---
s1.remove(10) # Remove the element 10 from the set s1. If 10 is present in s1, it will be removed; if 10 is not present, this will raise a KeyError because the remove() method does not allow for silent failure when trying to remove an element that is not in the set.
print("remove(10)  ->", s1)

# --- discard: delete if present; no error if missing ---
s1.discard(99)  # 99 is not in s1 — nothing happens
print("discard(99) ->", s1)

# --- pop: remove and return one arbitrary element ---
removed = s1.pop() # Remove and return an arbitrary element from the set s1. Since sets are unordered collections, the pop() method does not guarantee which element will be removed; it will remove and return some element from the set. If s1 is empty, this will raise a KeyError because there are no elements to pop.
print("pop()       -> removed:", removed, "| s1:", s1)

# --- update: add elements from another iterable (changes s1 in place) ---
s1.update({100, 200}) # Update the set s1 by adding elements from another iterable, in this case, the set {100, 200}. This will add the elements 100 and 200 to s1 if they are not already present. If either 100 or 200 is already in s1, it will not be added again since sets do not allow duplicate elements. The update() method modifies s1 in place, meaning that it changes the original set rather than creating a new one.
print("update({100, 200}) ->", s1)

# --- union: new set with all unique elements from both (s1 unchanged) ---
print("union(s2)   ->", s1.union(s2), "| s1 still:", s1) # Create a new set that is the union of s1 and s2, which will contain all unique elements from both sets. The union() method does not modify s1; it returns a new set that contains the combined unique elements of s1 and s2. The original set s1 remains unchanged after this operation.

# --- intersection: new set with elements in both (s1 unchanged) ---
print("intersection(s2) ->", s1.intersection(s2)) # Create a new set that is the intersection of s1 and s2, which will contain only the elements that are present in both sets. The intersection() method does not modify s1; it returns a new set that contains only the elements that are common to both s1 and s2. The original set s1 remains unchanged after this operation.

# --- issubset / issuperset: return True or False ---
small = {7, 8}  # every element here is also in s1
print("small.issubset(s1)   ->", small.issubset(s1))    # True — all of small is inside s1
print("s1.issuperset(small) ->", s1.issuperset(small))  # True — s1 contains all of small
print("s2.issubset(s1)      ->", s2.issubset(s1))       # False — 50 is in s2 but not in s1

# --- clear: remove all elements (do this last) ---
s1.clear() # Clear all elements from the set s1, resulting in an empty set. After calling clear(), s1 will contain no elements and will be represented as set() when printed. This method modifies s1 in place, meaning that it changes the original set rather than creating a new one.
print("clear()     ->", s1)
