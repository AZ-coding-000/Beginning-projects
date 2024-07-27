

life = True

while life == True:
    cd = input("Cooldown?:")
    atk = input("attack?:")

    dps = (1/float(cd))*int(atk)

    print(f'dps = {dps}')