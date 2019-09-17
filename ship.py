class Ship():
    def __init__(self, name, health, damage_amount):
        self.name = name
        self.health = health
        self.damage_amount = damage_amount

    def shoot_at(self, ship):
        ship.health -= self.damage_amount
        print("%s shot %s for %d damage" %
              (self.name, ship.name, self.damage_amount))
        if ship.health <= 0:
            print("%s was destroyed by %s" % (ship.title, self.name))
