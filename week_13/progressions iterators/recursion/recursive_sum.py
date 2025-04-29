class RecursiveSum:
    def __init__(self, n):
        self.n = n

    def sum(self):
        return self._recursive_sum(self.n)

    def _recursive_sum(self, n):
        if n == 0:
            return 0
        else:
            return n + self._recursive_sum(n - 1)

if __name__ == "__main__":
    n = 5
    recursive_sum = RecursiveSum(n)
    print(f"The sum of the first {n} natural numbers is: {recursive_sum.sum()}")