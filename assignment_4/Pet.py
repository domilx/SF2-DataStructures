from assignment_4 import Animal


class Pet(Animal):
    def __repr__(self) -> str:
        return "This animal is a pet!"

    def pet(self) -> str:
        return "You can pet this animal!"