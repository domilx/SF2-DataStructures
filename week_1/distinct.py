def distinct(year: int) -> int:
    year += 1
    while len(set(str(year))) < 4: year += 1
    return year
print(distinct(int(input("Enter a year: "))))