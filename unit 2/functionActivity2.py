# PROBLEM #1
# Create a function that will take in 2 inputs and 
# compare them.

# Your inputs should be numbers.

# The function should compareif the first input is
# less than the second input

# If it is less than the second input it
# should print true. If it is not, it should print false

def compareValue():
    valA= int(input())

print(valA < valB)




#Problem #2
# Create a function that will compare if a student
# has made honor roll

# The student should be able to input 2 pieces of data
# the first should be their grade and the second should
# be the number of days they have bee absent.

# if the student's grade is above a 90 and the number
# of absenses is less than 5, the program should print
# true, otherwise it should print false.

def check_honor_roll():
    grade = float(input(""90))
    absences = int(input("5 "))

    # Check conditions: grade above 90 and absences less than 5
    if grade > 90 and absences < 5:
        print("true")
    else:
        print("false")