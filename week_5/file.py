cubes = [(item, item**3) for item in range(1, 6)]

print(cubes)


multiples_of3  = [item for item in range(1, 30) if item % 3 == 0]

print(multiples_of3)

def isOdd(num):
    return num % 2 != 0

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered = filter(isOdd, nums)

print(list(filtered))

nums = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]

items = 0
sum =0
for row in nums:
    for num in row:
        sum += num
        items += 1

print(sum)
print(items)
print(int(sum / items))