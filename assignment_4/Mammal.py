from assignment_4 import Animal


class Mammal(Animal):
    def __repr__(self) -> str:
        return "Kingdom: Animalia\nClass: Mammal"

    def reproduce(self) -> None:
        print(
            "Members of this kingdom reproduce by finding a mate of the same species. "
            "Mammals give birth to live young and raise them until they can be independent."
        )