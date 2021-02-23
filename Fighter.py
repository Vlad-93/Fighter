class Fighter:
    name = ''
    hp = 100
    attack = 20

    def __init__(self, name, hp=100, attack=20):
        self.name = name
        self.hp = hp
        self.attack = attack

    def to_attack(self, unit):
        print(self.name, ' attack ', unit.name)
        unit.hp -= self.attack
        print(unit.name, ' hp = ', unit.hp)


unit1 = Fighter('Knight')
unit2 = Fighter('Archer', 80, 30)

while unit1.hp > 0 and unit2.hp > 0:
    unit1.to_attack(unit2)

    if unit2.hp <= 0:
        break

    unit2.to_attack(unit1)

if unit2.hp <= 0:
    print(unit1.name, ' - winner!')
elif unit1.hp <= 0:
    print(unit2.name, ' - winner!')
