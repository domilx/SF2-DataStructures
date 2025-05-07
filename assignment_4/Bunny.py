from assignment_4 import Herbivore, Heterotroph, Mammal, Pet


class Bunny(Herbivore, Mammal, Pet):
    legs: int = 4
    ears: int = 2

    def __repr__(self) -> str:
        return (
            "Kingdom: Animalia\n"
            "Class: Mammal\n"
            "Species: Bunny\n"
            f"{Pet.__repr__(self)}\n\n"
            f"{Heterotroph.__repr__(self)} "
            "This organism is a herbivore. It feeds on plant matter and its physiology facilitates food search."
        )

    def reproduce(self) -> None:
        print(
            "Members of this kingdom reproduce by finding a mate of the same species. "
            "Mammals give birth to live young and raise them until they can be independent. "
            "Bunnies can produce multiple litters per year, potentially having 3–8 kits per litter."
        )

    def eat(self) -> None:
        print("I eat other organisms instead of generating my own food.")
        print(
            "I eat mostly fresh hay and grass, with some leafy greens and a few pellets. "
            "I should only be given fruit and root vegetables, like carrots, as an occasional treat."
        )

    def move(self) -> None:
        print("I move by hopping and I can see behind me...")

    def sleep(self) -> None:
        print(
            "Bunnies are nocturnal animals, typically sleep around "
            "12 to 14 hours a day in short, intermittent periods."
        )