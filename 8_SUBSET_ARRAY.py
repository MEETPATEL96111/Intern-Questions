from itertools import *

s = [1, 2, 3, 4]
n = int(input("ENTER VALUE OF N = "))
perm = permutations(s, n)

# Print the obtained permutations 
for i in list(perm):
    print(list(i))