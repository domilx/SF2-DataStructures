from herbivore import Herbivore
from heterotroph import Heterotroph
from mammal import Mammal 
from pet import Pet


class Bunny(Herbivore, Mammal, Pet):
    legs: int = 4
    ears: int = 2

    def __repr__(self) -> str:
        return (
            f"{Mammal.__repr__(self)}\n"
            "Species: Bunny\n"
            f"{Pet.__repr__(self)}\n\n"
            f"{Herbivore.__repr__(self)}\n\n"
        )

    def reproduce(self) -> None:
        super().reproduce()
        print("Bunnies can produce multiple litters per year, potentially having 3-8 kits per litter.")

    def eat(self) -> None:
        super().eat()
        print(
            "I mostly eat fresh hay and grass, with some leafy greens and a few pellets. "
            "I should only be given fruit and root vegetables, like carrots, as an occasional treat."
        )

    def move(self) -> None:
        print("I move by hopping and I can see behind me...")

    def sleep(self) -> None:
        print(
            "Bunnies are nocturnal animals, typically sleep around "
            "12 to 14 hours a day in short, intermittent periods."
        )