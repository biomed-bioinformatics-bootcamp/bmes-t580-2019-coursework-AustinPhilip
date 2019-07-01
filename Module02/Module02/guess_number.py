# import library
import random

# pick and save a random number
gen_num = random.randint(0, 100) # generate random number
guess = 1000 # initialize guess
name = input('Name:  ') # input name

# pick a number
while guess != gen_num: #run until guess is equal to generated number
    guess_text = input('Pick a number between 0 and 100: ') # input guess
    guess = int(guess_text) # change to number

# decide if it's the right number
    if guess < gen_num:
        print('Sorry {}, {} was too low.'.format(name, guess)) # if guess is too large, say they were too high
    elif guess > gen_num:
        print('Sorry {}, {} was too high.'.format(name, guess)) # if guess to too small, say they were too low
    else:
        print('You did it {}! The number was {}!!'.format(name, guess)) # congratulate on getting it right

# play again?
print('Hit run to play again!!')