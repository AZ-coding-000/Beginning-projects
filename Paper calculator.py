print ("this calculator will tell you how thick an average peice of paper will be depending on how many times you fold it. Tt also tells you how large the surface area would be. Have fun!")

girth = float(0.05)
surface = float(603.2246)
life = True

while life == True:
    x = input ('number of folds: ')

    a = girth * (2 ** float(x))
    a2 = surface / (2** float(x))

    b = girth * (2 ** float(x))/1000
    b2 = (surface / (2** float(x)))*10

    c = girth * (2 ** float(x))/1000000
    c2 =  (surface / (2** float(x)))*1000000

    d = girth * (2** float(x))/1000000000
    d2 = (surface / (2 ** float(x)))*10000000000000

    e = girth * (2 ** float(x))/9461000000000000000

    print(f'{a} milimeters thick, {a2} square centimeters large,')
    print(f'{b} meters thick, {b2} square millimeters large,')
    print(f'{c} kilometers thick, {c2} square nanometers large.')
    print(f'{d} megameters thick, {d2} square phemptometers. ')
    print(f' {e} lightyears thick')

    
