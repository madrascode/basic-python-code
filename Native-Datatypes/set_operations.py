E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}

print("Union operation in python sets: ", E|N)

print("Intersection of E and N: ", E&N)

print("Difference of E and N: ", E-N) # will be considered for E... 

print("Symmetric Difference of E and N: ", E^N)  # jo dono sets me individually lie karta hai. 

# also we have in-built functions in python for set operations
print(E.union(N))
print(E.intersection(N))
print(E.difference(N))

print(E.symmetric_difference(N))