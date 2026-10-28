monster_health = 150
player_damage = 25

monsters = [monster_health, 100, 80]

for monster_number, health in enumerate(monsters, start=1):
    attacks = 0
    print(f"Monster {monster_number} wordt aangevallen!")

    while health > 0:
        health = max(0, health - player_damage)
        attacks += 1
        print(f"Health na aanval: {health}")

    print(f"Verslagen in {attacks} aanvallen.\n")