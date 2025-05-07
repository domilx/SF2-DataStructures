from bird import Bird
from heterotroph import Heterotroph
from omnivore import Omnivore
from pet import Pet

class Parrot(Bird, Omnivore, Pet):
    wings: int = 2
    legs: int = 2
    color: str = "green"

    def __repr__(self) -> str:
        return (
            f"{Bird.__repr__(self)}\n\n"
            "Species: Parrot\n"
            f"{Pet.__repr__(self)}\n\n"
            f"{Omnivore.__repr__(self)}\n\n"
        )

    def reproduce(self) -> None:
        print(
            super().reproduce() +
            "Bunnies can produce multiple litters per year, potentially having 3–8 kits per litter."
        )

    def eat(self) -> None:
        super().eat()
        print("I eat both plant and animal matter. My natural diet includes a variety of foods like seeds, nuts, fruits, vegetables, flowers, buds, and insects. ")

    def move(self) -> None:
        print("I can move in various ways. I can fly, climb and even use a unique method called ""beakiation"" to traverse narrow branches")

    def sleep(self) -> None:
        print("Parrots sleep around 10 to 12 hours each night, often tucked under their wings. They may also take naps during the day.")