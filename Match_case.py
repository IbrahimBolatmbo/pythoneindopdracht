player_class = "Paladin"

health = None
damage = None

match player_class:
    case "Warrior":
        health = 150
        damage = 20
    case "Mage":
        health = 80
        damage = 35
    case "Archer":
        health = 100
        damage = 25
    case "Rogue":
        health = 90
        damage = 30
    case "Paladin":
        health = 120
        damage = 15
    case "Necromancer":
        health = 70
        damage = 40
    case _:
        print(f"Onbekende class gekozen: {player_class}")

if health is not None and damage is not None:
    print(f"Class: {player_class}")
    print(f"Health: {health}")
    print(f"Damage: {damage}")