from progression import Progression

class FibonacciProgression(Progression):
    """
    Iterator producing a Fibonacci progression.
    
    default iterator produces the whole numbers
    """
    
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second
        self._current = second
    
    def _advance(self):
        """
        update self._current to a new value.
        """
        self._current, self._prev = self._prev + self._current, self._current

if __name__ == "__main__":
    print("Fibonacci Progression with default start values:")
    prog = FibonacciProgression()
    prog.printProgression(10)
    
    print("Fibonacci Progression with custom start values:")
    prog = FibonacciProgression(2, 3)
    prog.printProgression(10)
    
    print("Fibonacci Progression with custom start values and list output:")
    prog = FibonacciProgression(2, 3)
    print(prog.lstProgression(10))