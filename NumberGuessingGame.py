import random #imports the random function
print("Let's play a game.")
print("Enter a range of numbers.  I will then pick a number that you will try to guess!")

chosenNumber = None

while chosenNumber == None:

    try:   
        number1 = int(input("Please enter a number: ")) #This assigns the first number of the range


        number2 = int(input("Now enter a second number not equal to the previous number: ")) #Assigns the second number of the range


    except ValueError:
        print("Your answer is invalid. Please enter your values again!")
    
    else:
        if number1 > number2:
            chosenNumber = (random.randint(number2,number1))
            break
        elif number1 == number2:
            print("Those are the same numbers.  Choose again.")
        elif number1 < number2:
            chosenNumber = (random.randint(number1,number2))
            break
        else:
            print("Your answer is not valid.  Try again!")

guess = int
count = 0 

while guess != chosenNumber:
    try:

        guess = int(input("I have chosen a number. Please enter a guess: "))

    except ValueError:
        print("Your guess is invalid. Enter a number again!")

    else:
        if guess == chosenNumber:
            print("You guessed right! Congratulations!")
            print("Your number of guesses: " + str(count))
            break
        elif guess < chosenNumber:
            print ("Your guess was too low. Try again!")
            count += 1
        elif guess > chosenNumber:
            print ("Your guess was too high.  Try again!")
            count += 1
        else:
            print ("Your guess was not valid. Try again!")
            count += 1