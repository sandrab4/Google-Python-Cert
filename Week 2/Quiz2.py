name = "Diego"
fav_food = "lasagna"
print(name + "’s favorite food is " + fav_food) 
#should print Diego’s favorite food is lasagna


def clothing_type(temp):
    if temp>65:
        clothing = "T-Shirt"
    elif temp>50 and temp<=65:
        clothing = "Sweatshirt"
    elif temp>32 and temp<=50:
        clothing = "Jacket"
    else:
        clothing = "Heavy Coat"
    return clothing


print(clothing_type(72)) # Should print T-Shirt
print(clothing_type(55)) # Should print Sweatshirt
print(clothing_type(65)) # Should print Sweatshirt
print(clothing_type(50)) # Should print Jacket
print(clothing_type(45)) # Should print Jacket
print(clothing_type(32)) # Should print Heavy Coat
print(clothing_type(0)) # Should print Heavy Coat


def complementary_color(color):
    if color == "blue":
        complement = "orange"
    elif color == "yellow":
        complement = "purple"
    elif color == "red":
        complement = "green"
    else:
        complement = "unknown"
    return complement

print(complementary_color("blue")) # Should print orange
print(complementary_color("yellow")) # Should print purple
print(complementary_color("red")) # Should print green
print(complementary_color("black")) # Should print unknown
print(complementary_color("Blue")) # Should print unknown
print(complementary_color("")) # Should print unknown


def difference(x, y):
    z = x - y
    return z


print(difference(5, 3))
#should return 2


def fractional_part(numerator, denominator):
    # Operate with numerator and denominator to
    # keep just the fractional part of the quotient 
    if denominator == 0 or numerator == 0:
        part = 0
    else:
        part = (numerator%denominator)/denominator
    return part


print(fractional_part(5, 5)) # Should print 0
print(fractional_part(5, 4)) # Should print 0.25
print(fractional_part(5, 3)) # Should print 0.66...
print(fractional_part(5, 2)) # Should print 0.5
print(fractional_part(5, 0)) # Should print 0
print(fractional_part(0, 5)) # Should print 0