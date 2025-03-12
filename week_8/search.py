import time

def search(collection, value):
    print("searching")
    for i in collection:
        found = value in collection
    return found

lst = list(range(1, 50000))
s = set(range(1, 50000))

start = time.time()
print(search(s, 50000)) # False
print(time.time() - start)