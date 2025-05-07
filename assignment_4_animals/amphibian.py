from animal import Animal


class Amphibian(Animal):
    def __repr__(self) -> str:
        return super().__repr__() + "\nClass: Amphibian"

    def reproduce(self) -> None:
        super().reproduce()
        print("Amphibians reproduce by laying soft eggs in the water.")