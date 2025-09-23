import random

def test_random():
    random_number = random.randint(1, 20)
    print(random_number)
    round = 1
    guess_number = int(input("What is your guess number?"))

    while (round >= 6) :
        

        if guess_number == random_number :
            print("Congretulations")
        elif guess_number < random_number:
            print("Too low! Try again.")
        elif guess_number > random_number:
            print("too high! Try again.")
        round += 1
        if round > 6 :
            print("You lose")
    
test_random()