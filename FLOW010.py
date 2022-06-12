# cook your dish here
n = int(input())
for i in range(n):
    id = input()
    if id.lower()=='b':
        print("BattleShip")
    elif id.lower()=='c':
        print("Cruiser")
    elif id.lower()=='d':
        print("Destroyer")
    elif id.lower()=='f':
        print("Frigate")