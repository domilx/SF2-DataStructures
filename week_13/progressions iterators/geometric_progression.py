from progression import Progression

class GeometricProgression(Progression):
    """
    Iterator producing a geometric progression.
    
    default iterator produces the whole numbers
    """
    
    def __init__(self, start=1, base=2):
        super().__init__(start)
        self._base = base
    
    def _advance(self):
        """
        update self._current to a new value.
        """
        self._current *= self._base

if __name__ == "__main__":
    print("Geometric Progression with default start value:")
    prog = GeometricProgression()
    prog.printProgression(10)
    
    print("Geometric Progression with custom start value:")
    prog = GeometricProgression(3)
    prog.printProgression(10)
    
    print("Geometric Progression with custom start value and base:")
    prog = GeometricProgression(3, 3)
    prog.printProgression(10)
    
    print("Geometric Progression with custom start value, base and list output:")
    prog = GeometricProgression(3, 3)
    print(prog.lstProgression(10))