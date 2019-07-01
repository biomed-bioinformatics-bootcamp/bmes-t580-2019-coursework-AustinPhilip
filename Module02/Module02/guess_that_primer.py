# import library
import random
import string

# initialize game
bases = 'ACGTU' # bases available in DNA/RNA replication
gen_pri = random.choices(bases, k=5) # generate random order of bases in primer
lc_gen_pri1 = gen_pri[0].lower() # convert first base to lower case for matching
lc_gen_pri2 = gen_pri[1].lower() # convert second base to lower case for matching
lc_gen_pri3 = gen_pri[2].lower() # convert third base to lower case for matching
lc_gen_pri4 = gen_pri[3].lower() # convert fourth base to lower case for matching
lc_gen_pri5 = gen_pri[4].lower() # convert last base to lower case for matching
lc_gen_pri = [lc_gen_pri1,lc_gen_pri2,lc_gen_pri3,lc_gen_pri4,lc_gen_pri5] # combine bases into a single vector
guess = -1 # initialize guess
name = input('Welcome to Guess That Primer! To start, what is your name?  ') # input name
print ('Okay {}! Now try to guess order of the primer!'.format(name)) # explain what is happening

# pick your bases
while guess != lc_gen_pri: # run until correct
    guess_text1 = input('Pick your first of 5 bases (A C G T or U?): ') # input first base of primer
    guess_text2 = input('Pick your second of 5 bases (A C G T or U?): ') # input second base of primer
    guess_text3 = input('Pick your third of 5 bases (A C G T or U?): ') # input third base of primer
    guess_text4 = input('Pick your fourth of 5 bases (A C G T or U?): ') # input fourth base of primer
    guess_text5 = input('Pick your fifth of 5 bases (A C G T or U?): ') # input fifth base of primer
    guess = [guess_text1.lower(),guess_text2.lower(), guess_text3.lower(),guess_text4.lower(), guess_text5.lower()] # combine bases into a single vector

# decide if it's the right primer
    if guess == lc_gen_pri: # if the guess is correct
        print('You did it {}! You guessed the right primer!!'.format(name))
    else: # if guess is wrong
        print('Try again {}! '.format(name))
        if guess_text1 == lc_gen_pri1: # tells you if first base was right or wrong
            print('Your first base guess was right!')
        else:
            print('Your first base guess was wrong. Try a different base next time!')
        if guess_text2 == lc_gen_pri2: # tells you if second base was right or wrong
            print('Your second base guess was right!')
        else:
            print('Your second base guess was wrong. Try a different base next time!')
        if guess_text3 == lc_gen_pri3: # tells you if third base was right or wrong
            print('Your third base guess was right!')
        else:
            print('Your third base guess was wrong. Try a different base next time!')
        if guess_text4 == lc_gen_pri4: # tells you if fourth base was right or wrong
            print('Your fourth base guess was right!')
        else:
            print('Your fourth base guess was wrong. Try a different base next time!')

        if guess_text5 == lc_gen_pri5: # tells if last base was right or wrong
            print('Your fifth base guess was right!')
        else:
            print('Your fifth base guess was wrong. Try a different base next time!')

# play again?
print('Hit run to play again!!')