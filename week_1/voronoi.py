n = int(input("Number of villages: "))
villages = [int(input()) for i in range(n)]
villages.sort()

sizes = [] # hold the calculated neighborhood sizes

for i in range(1, n-1):
    sizes.append((villages[i] - villages[i-1]) + (villages[i+1] - villages[i]))

print(min(sizes))