from math import factorial as f

def binom(n, k):
    return f(n) // (f(k) * f(n - k)) 

print(binom(5, 3))
# this is O(n) time complexity

def pascale(n):
    for k in range(n + 1):
        print(binom(n, k))

print(pascale(5))
# this is O(n^2) time complexity


#make pascal as a list of sublists for a given n rows

def pascal(n):
    pascal = []
    
    for i in range(n):
        pascal.append([])
        for k in range(i + 1):
            pascal[i].append(binom(i, k))
    return pascal

print(pascal(5))
# this is O(n^2) time complexity

#make pascal as a list of sublists for a given n rows
# using list comprehension
pascal = lambda n: [[binom(i, k) for k in range(i + 1)] for i in range(n)]

print(pascal(5))


