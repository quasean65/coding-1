# What is a loops --> Code  thats repeats.

# While loops = a block code that repeats itself until the triggering
# condition is no longer TRUE. CAN BE INFINITE

# For loops = a type of loop (code block that repeats itself) BUT
# it only repeats itself upto a certain number of ties.
# IT IS FINITE

# THINK OF FOR LOOPS AS THE COUNTING LOOP = for --> 4 = number of loop

# FOR LOOP SYNTAX
# i stand for itertator = programmers decided make this the universal
# symbol for a placeholder for counting

for i in range(1, 6):
    print(i)

for i in "school":
    print(i)

# LIST --> A collection type that acts as a container for
# multiple data types and pieces of data.

# List Syntax 
# A list is written like a variable BUT after the equal assignment
# symbol we use SQUARE BRACKETS and put all of the datas inside of
# them

fooditem1 = "popcorn" # we can only store 1 piece of data in 1 variable

groceryList = ["popcorn", "apples", "water", ]
print(groceryList)

for groceryItem in groceryList:
    print("I need to buy"+ str(groceryItem))

itemPrices = [10.00, 20.00, 13.25, 7.95, 349.00]
tax = 0.07

for i in itemPrices:
    # I want to know how much in taxes i need to pay on each item
    print(tax *i)

    semesterGrades = [90, 100, 78, 76, 74, 82, 84]

    for i in semesterGrades:
        # I want to find ALL the grades lower than 85.
        if i < 85:
            print(i)
            