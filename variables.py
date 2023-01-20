#variables - aliases for a data value
variable = 0
jordy = 0
deez_nuts = 9

#primitive data types
#four primitives

#integers
#floats - number with a decimal
#boolean - True or False
#strings - ANYTHING in quotes '' or ""

#int
number = 0

#float
decimal = 7.9

#boolean (in Python it's bool)
toggle = True
toggle = False

#string
first_name = "brett"
last_name = "dale"

#below does NOT reference the above variable
name = "first_name"















#type casting - converting one variable's data type into another
#int
#float
#boolean
#string

#int to str
number = 8
number_as_a_string = str(number) # this becomes '0'
number_as_a_string = str(600) # this becomes '600'

#int to float
number = 7
decimal = float(number) # this becomes 7.0
decimal_as_string = str(decimal)
#print(decimal_as_string)


#float to int
number = 9.78
number_as_int = int(number) #this DOES NOT round - it truncates so it becomes 9
#print(str(number_as_int))




#string to bool
toggle = "true"
toggle = bool(toggle)
#print(toggle)




#concatenation -> Putting two or more strings together into one string
first_name = "jordy"
last_name = "arrasola"

#concatenation step
full_name = first_name + " " + last_name
print(full_name)
