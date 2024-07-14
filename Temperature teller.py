life = True

while life == True:

    temp = input('whats the tempurature outside, in farenheight?: ')

    if 3000 < int(temp):
        print('cut the crap, kid. Your lying. Thought it would be funny to put an absurdly big number, did you?')

    if 2200 <= int(temp) < 10000:
        print('Oh really? What volcano do you live in?')

    if 911 < int(temp) < 2200:
        print('Your not ok.')

    if 911 == int(temp):
        print('ALLAHUAKBAR')

    if 500 <= int(temp) < 911:
        print('Your not ok.')

    if 134 <= int(temp) < 500:
        print('new record! The current hottest temperature ever is 134. Must be global warming') 

    if 90 <= int(temp) < 134:
        print('Its boiling out there! dont go outside, trust me.')

    if 70 <= int(temp) < 90:
        print('wow, its hot today!')

    if 69 == int(temp):
        print ("( ͡° ͜ʖ ͡°)")

    if 58 <= int(temp) < 69 :
        print('its pretty nice outside!')

    if 40 <= int(temp) < 58:
        print('You should wear a hoodie today')

    if 30 <= int(temp) < 40:
        print('feels like jacket weather')

    if 0 <= int( temp) < 30:
        print('I dont recomend you even go outside.')

    if -144 <= int(temp) < 0:
        print('where do you live, the arctic?!')

    if -459 <= int(temp) < -144:
        print("where the hell do you live 💀")

    if int(temp) < -459:
        print('''you're lying. I know your lying because -459 degrees farenhiet is the lowest temperature physically possible. 
          stop messing around, kid.''')
    if temp == 'quit':
        life = False