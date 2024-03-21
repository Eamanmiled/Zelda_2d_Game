class Entity:
    hp = 100
    defe = 100
    att = 100

    def attack(self, increaseordecrease, amount):
        if increaseordecrease == "Increase":
            self.att = self.att + amount
        else:
            self.att = self.att - amount

    def defence(self, increaseordecrease, amount):
        if increaseordecrease == "Increase":
            self.defe = self.defe + amount
        else:
            self.defe = self.defe - amount

    def health(self, increaseordecrease, amount):
        if increaseordecrease == "Increase":
            self.hp = self.hp + amount
        else:
            self.hp = self.hp - amount

    def return_player_stats(self):
        print(self.hp)
        print(self.defe)
        print(self.att)


jake = Entity()
light_enemy = Entity()
derry = Entity()
alex = Entity()

jake.defence("Increase", 20)
derry.attack("decrease", 30)
jake.attack("Increase", 60)
jake.health("Increase", 20)
jake.return_player_stats()
derry.return_player_stats()
