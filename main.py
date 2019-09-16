import ship

destroyer = ship.Ship("Transporter", 100, 5)
pirate = ship.Ship("Pirate", 30, 10)

while destroyer.health > 0 and pirate.health > 0:
    pirate.shoot_at(destroyer)
    destroyer.shoot_at(pirate)
