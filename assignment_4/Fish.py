from assignment_4 import Animal


class Fish(Animal):
    def __repr__(self) -> str:
        return "Kingdom: Animalia\nClass: Fish"

    def reproduce(self) -> None:
        print(
            "Members of this kingdom reproduce by finding a mate of the same species. "
            "Fish reproduction varies largely; some give birth to live young while others lay eggs."
        )