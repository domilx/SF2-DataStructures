from assignment_4 import Mammal, Omnivore, Pet


class Dog(Omnivore, Mammal, Pet):
    legs: int = 4
    ears: int = 2

    def __repr__(self) -> str:
        return (
            "Kingdom: Animalia\n"
            "Class: Mammal\n"
            "Species: Dog\n"
            f"{Pet.__repr__(self)}"
        )

    def reproduce(self) -> None:
        print(
            "Members of this kingdom reproduce by finding a mate of the same species. "
            "Mammals give birth to live young and raise them until they can be independent. "
            "Dogs typically have litters of 5–6 puppies."
        )

    def eat(self) -> None:
        print("I eat other organisms instead of generating my own food.")
        print("I eat meat, vegetables, and dog treats.")

    def move(self) -> None:
        print("I move by walking or running on my four legs.")

    def sleep(self) -> None:
        print("Dogs typically sleep 12 to 14 hours a day.")