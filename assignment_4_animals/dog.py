from mammal import Mammal
from omnivore import Omnivore
from pet import Pet


class Dog(Omnivore, Mammal, Pet):
    legs: int = 4
    ears: int = 2

    def __repr__(self) -> str:
        return (
            f"{Mammal.__repr__(self)}\n\n"
            "Species: Dog\n"
            f"{Pet.__repr__(self)}"
            f"{Omnivore.__repr__(self)}\n\n"
        )

    def reproduce(self) -> None:
        super().reproduce()
        print("Dogs typically have litters of 5-6 puppies.")

    def eat(self) -> None:
        super().eat()

    def move(self) -> None:
        print("I move by walking or running on my four legs.")

    def sleep(self) -> None:
        print("Dogs typically sleep 12 to 14 hours a day.")