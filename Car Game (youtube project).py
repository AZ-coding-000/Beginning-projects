#Car game


life = True
print(""" Welcome to Car Racing Simulator!
      Your available commands are:
      Start: start the car.
      Stop: Shut off the car.
      Quit: Close the Simulator.
      Side note: any other command will not work.
       """)

on =False

while True:
    inputin = input(">").lower()
    
    if inputin == "start" and on == False:
        print("Car is on now. Ready to roll!")
        on = True

    elif inputin == "start" and on ==True:
        print("The car is already on.")
    
    elif inputin == "stop" and on ==True:
        print("Car is off now. Waiting for use again.")
        on=False

    elif inputin == "stop" and on ==False:
        print("The car is already off.")

    elif inputin == "quit":
        print("Hope you had fun!")
        break

    else:
        print("I don't understand.")
        