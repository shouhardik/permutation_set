from itertools import permutations
perm = permutations([1, 2, 3])
for i in list(perm):
	print i

# Expected Answer->(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)
