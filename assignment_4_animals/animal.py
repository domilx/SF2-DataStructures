class Animal:
    legs: int = 0
    fins: int = 0

    def __repr__(self) -> str:
        return "Kingdom: Animalia"

    def reproduce(self) -> None:
        print("Members of this kingdom reproduce by finding a mate of the same species.")
