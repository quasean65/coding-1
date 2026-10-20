# Loop - a loop is a construct (special function) that repeats itself.
# In programming, a loop allows to repeat code instructions.

# There are two types of loops: For loop  and While loop

# While loop - a type of loop where so long as a condition is equal
# to true it will keep running "forever".

# the keyword is while --> do while

# syntax
num = 4
while 2+2 == num: # Condition --> Operations - must be TRUE
     print("the program is running...")
     num = int(input("Please type in any number but 4 to stop the program"

     # While loops will ALWAYS run unless you change the condition!
     # we can dp this by writing instructions to manually change it.
     # The computer must ALWAYS complete their tasks before moving to the
     # next step


    def guessingGames():
        correctAmswer=  8
        attempts = 0
        print("WELCOME TO THE GUESSING GAME")
        print("Please type in a number betweem 1 and 10")
        userGuess = int(input("Please type in a number"))
        while userGuess != correctAmswer