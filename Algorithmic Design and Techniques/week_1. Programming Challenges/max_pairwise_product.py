# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

index_1 = 0

for i in range(1, n):
	if a[i] > a[index_1]:
		index_1 = i
    
if index_1 == 0:
	index_2 = 1
else:
	index_2 = 0
    
for j in range(1, n):
	if (index_1 != j) and (a[j] > a[index_2]):
		index_2 = j
    
print(a[index_1] * a[index_2])