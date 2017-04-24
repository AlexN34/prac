import random

num = random.randint(1, 20)

gameState = False
nGuesses = 1
g = int(input('I am thinking of a number between 1 and 20.\nTake a guess.\n').strip())
while gameState is False:
    if nGuesses >= 6 or g == num:
        nGuesses += 1
        break
    elif g < num:
        g = int(input ('Your guess is too low.\nTake a guess.\n').strip())
        nGuesses += 1
    elif g > num:
        nGuesses += 1
        g = int(input ('Your guess is too high.\nTake a guess.\n').strip())

if nGuesses <= 6:
    print ("Good job! You guessed my number in %d guesses!\n" % (nGuesses))
else:
    print ("Nope. The number I was thinking of was %d" % (num))

