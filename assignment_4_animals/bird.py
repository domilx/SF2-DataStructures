from animal import Animal


class Bird(Animal):
    def __repr__(self) -> str:
        return super().__repr__() + "\nClass: Bird"

    def reproduce(self) -> None:
        super().reproduce()
        print("Birds typically reproduce by hatching and incubating their eggs.")