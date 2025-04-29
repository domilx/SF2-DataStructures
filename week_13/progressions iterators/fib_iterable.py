class FibonacciIterable:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        self.a, self.b = 0, 1
        return self

class FibonacciIterable:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        self.a, self.b = 0, 1
        return self
    
    def __next__(self):
        if self.a > self.n:
            raise StopIteration
        else:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            return result