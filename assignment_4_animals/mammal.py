from animal import Animal


class Mammal(Animal):
    def __repr__(self) -> str:
        return super().__repr__() + "\nClass: Mammal"

    def reproduce(self) -> None:
        super().reproduce()
        print("Mammals give birth to live young and raise them until they can be independent.")