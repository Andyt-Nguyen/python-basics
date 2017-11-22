#String Functions

myStr = 'Hello World'

#Capitalize
print(myStr.capitalize())

#Swap case
print(myStr.swapcase())

#Get Length
print(len(myStr))

#Replace
print(myStr.replace('World', "Everyone"))

#Count
target = 'l'
print(myStr.count(target))

#Startswith
print(myStr.startswith('H'))

#Endswith
print(myStr.endswith('d'))

#Split to list
print(myStr.split())

#Find
splitter = myStr.split()
print(myStr.find('World'))

#Index
print(myStr.index('H'))

#Alphanumeric
print(myStr.isalnum())

#Alphabetic
print(myStr.isalpha())

#Numeric
print(myStr.isnumeric())