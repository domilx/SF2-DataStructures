"""
Firgus is behind on several assignments.
After rummaging thru his backpack, he realizes
he has N items, each of which he records as a string
he has M upcoming assignments, the i-th of which
requests T_i items to complete, r1, r2, ..., rT_i

If he has T_i required items, he can complete the i-th assignment
Otherwise, he flunks the assignment
How many assignments can he complete?

INPUTS:
--> first line: N M
    - N: number of items in Firgus's backpack
    - M: number of assignments
--> next N lines: each line contains a string
    - string is always unique
--> next M sections:
    - contain a single integer Ti followed by T_i lines each ontaining a string

OUTPUT:
    - number of assignments Firgus can complete

sample:
3 4
chalk
cheese
charger
1
cheese
2
coins
cash
3
charger
chalk
caffeine
3
cheese
charger
chalk

output:
2
"""

n, m = input().split()
items = set()
assignments = []
for _ in range(int(n)): items.add(input())
for _ in range(int(m)):
    assignment = set()
    for _ in range(int(input())): assignment.add(input())
    assignments.append(assignment)
print(sum(1 for assignment in assignments if all(item in items for item in assignment)))