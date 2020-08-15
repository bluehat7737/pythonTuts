class Emp:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def define(self):
        return f"Employee name is {self.name} and it's role is {self.role}"


class Player:
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def pdefine(self):
        return f"Player name is {self.name} and game is {self.game}"


class coolemp(Emp, Player):
    pass

anshul = coolemp("Anshul", "Prog")

print(anshul.define())