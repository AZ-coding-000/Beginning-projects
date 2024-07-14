#Full atom weight

life = True

print("""This displays the weight of an object if the nucleus of its atoms where as big as the atom itself. no decimal points
    
    """)



while life == True:
    weight = input("Weight (in pounds): ")

    x = (int(weight) * 250000000000000)/2205000000
    y = (int(weight) * 25000000000000)/2205
    z = int(weight) * 25000000000000

    print(f"""{x} megatonnes,
    {y} tonnes,
    {z} pounds"""
          )
