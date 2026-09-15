# Assigment Operators- Exclusively used to
# assign values to variables. 
# think key / value pairings 

# We use a sinmgle equal sign to represent the assingment 
# operator
name = Qua'sean 
grade = 10
school = Boys latin

# Arithmetic Operqtors- Used on numerical
# data types to perform calculations.
# intergers ( whole numbers) an floats (decimal numbers)

# print is a function that lets us show code 
# in the terminal

# Comparison Operators - set of symbols used
# to asses if data is the same or different and
# how they differ

print(10 > 1)
print(2000 < 100)

# 2 equal signs compare if something is the SAME 
print ("book" == "Book") # same as (FALSE)
print("2" == 2 ) # same as (false)
print(2.0 == 2)

# not equal is written with !
# this is to check and filter for values that are not
# the same
# side note - exclamtion ALWAYS means NOT in
# programming
print(200 != 100)
print(300 !=300)


# logical operators- compares 2 conditions to check if 
# they are true or false
# conditions = other operations
# instead of symbols, we represent these with words:
# and, or , not

# AND - checks if 2 conditions are true. if yes,
# result is true
print(3 > 1 and 100 == 50) # this would come out to be true

# OR- checks if only 1 condition is true. if yes,
# the final result will be true
print(3 > 1 or 100 == 50)


# NOT - the "opposite day" operator. it will reverse the
# result of the logical operators
print(not(3 >1 and 100 >500))
# this would come out to be false