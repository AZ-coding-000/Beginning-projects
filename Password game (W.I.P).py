e = 'Error'
error = False
good_password = False

while good_password == False:

    password = input("make a password ")

    if len(password) < 15:
        print(f'{e}, not enough characters') 
        error = True

    if password == float:
        print(f'{e}, has a decimal point')
        error = True

    if len(password) > 15:
        print(f'{e}, too many characters')
        error = True


    if error == False:
        print("Valid Password")
        good_password = True