class Progression:
    """
    iterator producing a generic progression.
    
    default iterator produces the whole numbers
    """
    
    def __init__(self, start=0):
        self._current = start
    
    def _advance(self):
        """
        update self._current to a new value.
        """
        self._current += 1
    
    def __next__(self):
        """
        return the next element, or raise StopIteration error.
        """
        if self._current is None:
            raise StopIteration
        else:
            answer = self._current
            self._advance()
            return answer
    
    def __iter__(self):
        """
        return self iterator object.
        """
        return self
    
    def printProgression(self, n):
        """
        print the next n values of the progression.
        """
        print(" ".join(str(next(self)) for j in range(n)))
    
    def lstProgression(self, n):
        """
        return the next n values of the progression as a list.
        """
        return [int(next(self)) for j in range(n)]
    
if __name__ == "__main__":
    print("Progression with default start value:")
    prog = Progression()
    prog.printProgression(10)
    
    print("Progression with custom start value:")
    prog = Progression(5)
    prog.printProgression(10)
    
    print("Progression with custom start value and list output:")
    prog = Progression(5)
    print(prog.lstProgression(10))