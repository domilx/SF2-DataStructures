from assignment_4 import Animal


class Reptile(Animal):
    def __repr__(self) -> str:
        return "Kingdom: Animalia\nClass: Reptile"

    def reproduce(self) -> None:
        print(
            "Members of this kingdom reproduce by finding a mate of the same species. "
            "Reptiles reproduce by laying eggs, typically on land rather than water."
        )