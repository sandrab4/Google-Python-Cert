#Practice Quiz 1 "Expressions and Variables" Week 2


print("2 + 2 = " + str(2 + 2))
#should print 2 + 2 = 4


bill = 47.28 # Assign "bill" variable with bill amount
tip = bill * 0.15 # Multiply by stated tip rate 
total = bill + tip # Sum the "total" of the "bill" and "tip"
share = total/2 # Divide "total" by number of friends dining
print("Each person needs to pay: " + str(share)) # Enter the required string and "share" 
# Hint: Remember to convert incompatible data types
#should print Each person needs to pay: 27.186


numerator = 10
denominator = 10
result = numerator / denominator
print(result)
#should print 1.0


word1 = "How"
word2 = " do"
word3 = " you"
word4 = " like"
word5 = " Python"
word6 = " so"
word7 = " far?"

print(word1 + word2 + word3 + word4 + word5 + word6 + word7)
#should print How do you like Python so far?


#Practice Quiz 2 "Functions" Week 2


# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

# Do not indent any of the following lines of code as they are 
# meant to be located outside of the function above

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the my_trip_km conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result of
#    my_trip_km. Fill in the blank to print the result.
round_trip_km = my_trip_km * 2
print("The round-trip in kilometers is " + str(round_trip_km))
#should print The distance in kilometers is 88.0
#The round-trip in kilometers is 176.0


# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)
#should print 99 100


def print_seconds(hours, minutes, seconds):
    print(hours*3600+minutes*60+seconds)


print_seconds(1,2,3)
#output will print to the screen
#should print 3723


#Practice Quiz 3 "Conditionals" Week 2


def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))
#should print Welcome back Taylor!
#Hello there, John


if number > 11: 
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)
#should print 2


x= "A dog"
y= "A mouse"
print(x<y or x>y)

a= "9999+8888"
b= "100*100"
print(a<b or a>b)
#should print True
#True


def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return (full_blocks + 1) * block_size
    return filesize

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192