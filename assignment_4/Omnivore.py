from assignment_4 import Heterotroph


class Omnivore(Heterotroph):
    def __repr__(self) -> str:
        return (
            super().__repr__() +
            " This organism is an omnivore. It feeds on both plants and other animals."
        )

    def eat(self) -> None:
        print("I eat other organisms instead of generating my own food.")
        print("I eat anything!")