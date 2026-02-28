# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).


#== is comparison, changed to = for assignment. also, int.input is wrong, changed to int(input for format
year = int(input("Greetings! What is your year of origin?")) #matched opening and closing quotation marks

if year <= 1900: #missing colon
    print ("Woah, that's the past!") #double quotes for the text output
elif 1900 < year < 2020: #can also use 'and' but felt more consice to just use 1900 < year < 2020
    print ("That's totally the present!")
else: #condition for elif was missing, replaced with else
    print ("Far out, that's the future!!")

