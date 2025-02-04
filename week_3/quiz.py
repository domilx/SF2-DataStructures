def divisors(n):
    divs = []
    num = abs(n)
    while num >= 0:
        if num != 0:
            if n % num == 0:
                divs.append(num)
        else:
            num = -1
        num = num - 1
    return divs

print(divisors(int(input())))