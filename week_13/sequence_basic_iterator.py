class SequenceIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return Sequence(self.start, self.end)
    
    def __len__(self):
        return self.end - self.start + 1

class Sequence:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            result = self.start
            self.start += 1
            return result
        else:
            raise StopIteration

if __name__ == "__main__":
    seq = SequenceIterable(3,10)
    
    print("Length before iteration:")
    print(len(seq))
    
    print("Iterating over the sequence:")
    for i in seq:
        print(i)
    
    print("Length after iteration:")
    print(len(seq))
    
    print("Iterating over the sequence again:")
    for i in seq:
        print(i)