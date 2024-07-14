life = True

print ('santa decides to go on a sugar diet and gives all 8 billion cookies he collected this christmas to a newborn. assuming the newborn cant get diabetes and will die at about 72.5 years of age, input a number for the amount of cookies he can eat in a day and this calculator will tell you how long he will last')

while life == True:
    #cpd is cookies per day
    #72.5 years in a human life
    #306099
    #306400
    #306500
    #306510
    #306513
       
    cpd = input('Number: ')

    a = (8000000000 / (int(cpd)*360))

    print (f' This guy can last can last for {a} years ')