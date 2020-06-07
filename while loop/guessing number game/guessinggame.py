secret_number = 5
guess_count = 0
while guess_count < 3:
    guess_number = int(input("guess_number: "))
    guess_count += 1
    if guess_number == secret_number:
        print("You won !")
        break 
else:
    print("Sorry U have guessed it wrong !")
