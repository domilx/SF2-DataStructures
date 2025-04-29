from progression import Progression

class ArithmeticProgression(Progression):
    """
    Iterator producing an arithmetic progression.
    
    default iterator produces the whole numbers
    """
    
    def __init__(self, start=0, increment=1):
        super().__init__(start)
        self._increment = increment
    
    def _advance(self):
        """
        update self._current to a new value.
        """
        self._current += self._increment

if __name__ == "__main__":
    print("Arithmetic Progression with default start value:")
    prog = ArithmeticProgression()
    prog.printProgression(10)
    
    print("Arithmetic Progression with custom start value:")
    prog = ArithmeticProgression(5)
    prog.printProgression(10)
    
    print("Arithmetic Progression with custom start value and increment:")
    prog = ArithmeticProgression(5, 2)
    prog.printProgression(10)
    
    print("Arithmetic Progression with custom start value, increment and list output:")
    prog = ArithmeticProgression(5, 2)
    print(prog.lstProgression(10))