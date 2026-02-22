E = [0, 2, 4, 6, 8]
N = [1, 2, 3, 4, 5]
union = []
for i in E:
    if i not in union:
        union.append(i)
for i in N:
    if i not in union:
        union.append(i)
intersection = []
for i in E:
    if i in N:
        intersection.append(i)
difference = []
for i in E:
    if i not in N:
        difference.append(i)
sym_diff = []
for i in union:
    if i not in intersection:
        sym_diff.append(i)

print("Union of E and N is", union)
print("Intersection of E and N is", intersection)
print("Difference of E and N is", difference)
print("Symmetric difference of E and N is", sym_diff)
