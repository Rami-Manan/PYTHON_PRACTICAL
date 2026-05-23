# Set object methods — each section shows one method and its result

s1 = {3, 4, 6, 7, 8, 9}  # unordered collection of unique elements
s2 = {7, 8, 50}          # second set (50 is only in s2 — useful for union / intersection)

print("Original s1:", s1)
print()

# --- add: insert one element ---
s1.add(10)
print("add(10)     ->", s1)

# --- remove: delete element (raises KeyError if missing) ---
s1.remove(10)
print("remove(10)  ->", s1)

# --- discard: delete if present; no error if missing ---
s1.discard(99)  # 99 is not in s1 — nothing happens
print("discard(99) ->", s1)

# --- pop: remove and return one arbitrary element ---
removed = s1.pop()
print("pop()       -> removed:", removed, "| s1:", s1)

# --- update: add elements from another iterable (changes s1 in place) ---
s1.update({100, 200})
print("update({100, 200}) ->", s1)

# --- union: new set with all unique elements from both (s1 unchanged) ---
print("union(s2)   ->", s1.union(s2), "| s1 still:", s1)

# --- intersection: new set with elements in both (s1 unchanged) ---
print("intersection(s2) ->", s1.intersection(s2))

# --- issubset / issuperset: return True or False ---
small = {7, 8}  # every element here is also in s1
print("small.issubset(s1)   ->", small.issubset(s1))    # True — all of small is inside s1
print("s1.issuperset(small) ->", s1.issuperset(small))  # True — s1 contains all of small
print("s2.issubset(s1)      ->", s2.issubset(s1))       # False — 50 is in s2 but not in s1

# --- clear: remove all elements (do this last) ---
s1.clear()
print("clear()     ->", s1)
