from assignment_4 import Heterotroph


class Carnivore(Heterotroph):
    def __repr__(self) -> str:
        return (
            super().__repr__() +
            " This organism is a carnivore. It feeds on other animals, and its physiology features facilitate hunting."
        )

    def eat(self) -> None:
        print("I eat other organisms instead of generating my own food.")
        print("I eat meat.")