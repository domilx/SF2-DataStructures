franchises, days = map(int, input().split())
sales = []

for i in range(days):
    sales.append(list(map(int, input().split())))

def calculateRowSales(all_sales: list) -> list:
    num = []
    for i in all_sales: num.append(sum(i))
    return num

def calculateColumnSales(all_sales: list) -> list:
    num = []
    for i in range(len(all_sales[0])):
        total = 0
        for j in range(len(all_sales)):
            total += all_sales[j][i]
        num.append(total)
    return num


def __main__():
    nums = calculateRowSales(sales) + calculateColumnSales(sales)
    bakersDozens = 0
    for i in nums:
        if i % 13 == 0:
            bakersDozens += i // 13
    print(bakersDozens)

__main__()