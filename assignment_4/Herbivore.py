from assignment_4 import Heterotroph


class Herbivore(Heterotroph):
    def __repr__(self) -> str:
        return (
            super().__repr__() +
            " This organism is a herbivore. It feeds on plant matter and its physiology facilitates food search."
        )

    def eat(self) -> None:
        print("I eat other organisms instead of generating my own food.")
        print("I eat plants.")