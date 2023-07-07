# Assesment Week 4



def format_address(address_string):


    house_number = ""
    street_name = ""


    # Separate the house number from the street name.
    address_parts = address_string.split()
    
    for address_part in address_parts:
       # Complete the if-statement with a string method.  
       if address_part.isdigit():
         house_number = address_part
       else:
         street_name += address_part + " "
    # Remove the extra space at the end of the last "street_name".
    street_name = street_name.strip()
 
    # Use a string method to return the required formatted string.
    return "House number " + house_number + " on a street named " + street_name
print(format_address("123 Main Street"))
# Should print: "House number 123 on a street named Main Street"
print(format_address("1001 1st Ave"))
# Should print: "House number 1001 on a street named 1st Ave"
print(format_address("55 North Center Drive"))
# Should print "House number 55 on a street named North Center Drive"




def highlight_word(sentence, word):
    # Complete the return statement using a string method.
    highlighted_sentence = sentence.replace(word, word.upper())
    return highlighted_sentence

print(highlight_word("Have a nice day", "nice"))
# Should print: "Have a NICE day"
print(highlight_word("Shhh, don't be so loud!", "loud"))
# Should print: "Shhh, don't be so LOUD!"
print(highlight_word("Automating with Python is fun", "fun"))
# Should print: "Automating with Python is FUN"



def alphabetize_lists(list1, list2):


  new_list = Imanis_list # Initialize a new list.
  new_list = list1 + list2 # Combine the lists.
  new_list.sort() # Sort the combined lists.
  return new_list 


Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]


print(alphabetize_lists(Aniyahs_list, Imanis_list))
# Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']



def squares(start, end):
    return [ x**2 for x in range(start, end+1) ] # Create the required list comprehension.


print(squares(2, 3)) # Should print [4, 9]
print(squares(1, 5)) # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



def car_listing(car_prices):
  result = ""
  # Complete the for loop to iterate through the key and value items 
  # in the dictionary.
  for car, price in car_prices.items():
    result += "A {} costs {} dollars\n".format(car, price) # Use a string method to format the required string. 
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Should print:
# A Kia Soul costs 19000 dollars
# A Lamborghini Diablo costs 55000 dollars
# A Ford Fiesta costs 13000 dollars
# A Toyota Prius costs 24000 dollars



def combine_guests(guests1, guests2):
    combined_guests = guests2.copy()  # Create a copy of guests2 to preserve its original data
    
    combined_guests.update(guests1)  # Update the combined_guests dictionary with guests1
    
    return combined_guests

Ricks_guests = {
    "Adam": 2,
    "Camila": 3,
    "David": 1,
    "Jamal": 3,
    "Charley": 2,
    "Titus": 1,
    "Raj": 4
}

Tessas_guests = {
    "David": 4,
    "Noemi": 1,
    "Raj": 2,
    "Adam": 1,
    "Sakira": 3,
    "Chidi": 5
}

print(combine_guests(Ricks_guests, Tessas_guests))



def count_letters(text):
  # Initialize a new dictionary.
  dictionary = {} 
  # Complete the for loop to iterate through each "text" character and 
  # use a string method to ensure all letters are lowercase.
  for char in text.lower(): 
    # Complete the if-statement using a string method to check if the
    # character is a letter.
    if char.isalpha(): 
      # Complete the if-statement using a logical operator to check if 
      # the letter is not already in the dictionary.
      if char not in dictionary: 
           # Use a dictionary operation to add the letter as a key
           # and set the initial count value to zero.
           dictionary[char] = 0  
      # Use a dictionary operation to increment the letter count value 
      # for the existing key.
      dictionary[char] += 1  
      ___ # Increment the letter counter. 
  return dictionary

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}