import random
number=input("Type a Number: ")
if number.isdigit():
    number=int(number)
    if number<=0:
        print("Please type a number greater than 0.")
        quit()
else:
    print("Please type a number.")
    quit()
random_number=random.randint(0,number)
guesses=0
while 1:
    guesses+=1
    user_guess=input("Make a Guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please type a number.")
        continue
    if user_guess==random_number:
        print("Hurray!,you got it")
        break

    elif user_guess>random_number:
        print("You were above the number!")
    else:
        print("you were below the number!")
print("You got in",guesses,"guesses")