import random
x = random.randint(1,100)
guess = float(input("Enter your guess for the square root of {}: ".format(x)))

if guess*guess == x:
    print("You guessed it right.")
else:
    for i in range(20):
        approximation = (guess + x/guess)/2
        guess = approximation
        if i == 1:
            print("The {}st guess is {}".format(i,guess))
        elif i == 2:
            print("The {}nd guess is {}".format(i,guess))
        elif i == 3:
            print("The {}rd guess is {}".format(i,guess))
        else:
            print("The {}th guess is {}".format(i,guess))