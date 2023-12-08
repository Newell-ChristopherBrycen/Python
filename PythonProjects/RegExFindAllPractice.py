import re

phoneRegex = re.compile(r'((\d\d\d)?-(\d\d\d-\d\d\d\d))')

mine = 'My numbers are 415-555-1234, 555-4242, 212-555-0000'

phoneRegex.search(mine)
phoneRegex.findall(mine) # returns a list of strings, not a match in like search does

# christmas example
lyrics = '''12 drummers drumming,
11 pipers piping,
10 lords a-leaping,
9 ladies dancing,
8 maids a-milking,
7 swans a-swimming,
6 geese a-laying,
5 gold rings,
4 calling birds,
3 French hens,
2 turtle doves,
And 1 partridge in a pear tree!'''

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

# --- Create your own
vowelRegex = re.compile(r'[aeiouAEIOU]') # r'(a|e|i|o|u)'

print(vowelRegex.findall('Robocop eats baby food'))

consonantsRegex = re.compile(r'[^aeiouAEIOU]') # ^ indicates to do the opposite

print(consonantsRegex.findall('Robocop eats baby food'))
