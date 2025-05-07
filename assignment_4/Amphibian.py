from assignment_4 import Animal


class Amphibian(Animal):
    def __repr__(self) -> str:
        return "Kingdom: Animalia\nClass: Amphibian"

    def reproduce(self) -> None:
        print(
            "Members of this kingdom reproduce by finding a mate of the same species. "
            "Amphibians reproduce by laying soft eggs in the water."
        )