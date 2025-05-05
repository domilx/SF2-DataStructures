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


class Omnivore(Heterotroph):
    def __repr__(self) -> str:
        return (
            super().__repr__() +
            " This organism is an omnivore. It feeds on both plants and other animals."
        )

    def eat(self) -> None:
        print("I eat other organisms instead of generating my own food.")
        print("I eat anything!")


class Herbivore(Heterotroph):
    def __repr__(self) -> str:
        return (
            super().__repr__() +
            " This organism is a herbivore. It feeds on plant matter and its physiology facilitates food search."
        )

    def eat(self) -> None:
        print("I eat other organisms instead of generating my own food.")
        print("I eat plants.")


class Carnivore(Heterotroph):
    def __repr__(self) -> str:
        return (
            super().__repr__() +
            " This organism is a carnivore. It feeds on other animals, and its physiology features facilitate hunting."
        )

    def eat(self) -> None:
        print("I eat other organisms instead of generating my own food.")
        print("I eat meat.")


class Animal:
    legs: int = 0
    fins: int = 0

    def __repr__(self) -> str:
        return "Kingdom: Animalia"

    def reproduce(self) -> None:
        print("Members of this kingdom reproduce by finding a mate of the same species.")


class Pet(Animal):
    def __repr__(self) -> str:
        return "This animal is a pet!"

    def pet(self) -> str:
        return "You can pet this animal!"


class Mammal(Animal):
    def __repr__(self) -> str:
        return "Kingdom: Animalia\nClass: Mammal"

    def reproduce(self) -> None:
        print(
            "Members of this kingdom reproduce by finding a mate of the same species. "
            "Mammals give birth to live young and raise them until they can be independent."
        )


class Fish(Animal):
    def __repr__(self) -> str:
        return "Kingdom: Animalia\nClass: Fish"

    def reproduce(self) -> None:
        print(
            "Members of this kingdom reproduce by finding a mate of the same species. "
            "Fish reproduction varies largely; some give birth to live young while others lay eggs."
        )


class Reptile(Animal):
    def __repr__(self) -> str:
        return "Kingdom: Animalia\nClass: Reptile"

    def reproduce(self) -> None:
        print(
            "Members of this kingdom reproduce by finding a mate of the same species. "
            "Reptiles reproduce by laying eggs, typically on land rather than water."
        )


class Amphibian(Animal):
    def __repr__(self) -> str:
        return "Kingdom: Animalia\nClass: Amphibian"

    def reproduce(self) -> None:
        print(
            "Members of this kingdom reproduce by finding a mate of the same species. "
            "Amphibians reproduce by laying soft eggs in the water."
        )


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