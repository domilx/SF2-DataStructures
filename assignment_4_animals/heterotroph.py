class Heterotroph:
    legs: int = 0
    fins: int = 0

    def __repr__(self) -> str:
        return (
            "This organism is a heterotroph. "
            "It is unable to produce its own food, so it eats other organisms."
        )

    def eat(self) -> None:
        print("I eat other organisms instead of generating my own food.")