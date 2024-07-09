class Game:
    def _init_(self):
        self.user = self.get_user_item()

    @staticmethod
    def get_user_item():
        user = input("Select (r)ock, (p)aper, (s)cissors: ")
        while user not in list("rps"):
            user = input("Please enter a valid input: ")
        return user