import re

#--------testing the ? regular expression (0 or 1)
batRegex = re.compile(r'Bat(wo)?man')

mo1 = batRegex.search('The Adventures of Batman') 
mo2 = batRegex.search('The Adventures of Batwoman')
mo3 = batRegex.search('The Adventures of Batwowowoman')

mo1.group()# returns batman
mo2.group()# returns batwoman
mo3 == None # returns true because (wo) is defined to be allowed to appear 0 or 1 times


phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
phoneRegex.search('My phone number is 555-555-5555. Call me tomorrow.')
phoneRegex.search('My phone number is 555-5555. Call me tomorrow.')

#-------testing the * expression (0 or more)

batRegex2 = re.compile(r'Bat(wo)*man')

mo4 = batRegex2.search('The Adventures of Batman') # returns batman
mo5 = batRegex2.search('The Adventures of Batwoman')# returns batwoman
mo6 = batRegex2.search('The Adventures of Batwowowoman') # this works because of *

#------ testing the + expression (1 or more)

batRegex3 = re.compile(r'Bat(wo)+man')

mo7 = batRegex3.search('The Adventures of Batman') # mo7 == none : returns true the "wo" never shows in entry
mo8 = batRegex3.search('The Adventures of Batwoman') # returns batwoman
mo9 = batRegex3.search('The Adventures of Batwowowoman')

#----- Using literal +, *, and ? in expressions

regex = re.compile(r'(\+\*\?)+')
mo10 = regex.search('I can use the +*? regex syntax')


#---------searching for repeating
phone2Regex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(, )?){3}')
mo11 = phone2Regex.search('My numbers are 415-555-1234, 555-4242, 212-555-0000')

#--------searching for range

digitRegex = re.compile(r'(\d){3,5}') # "greedy" match
digit2Regex = re.compile(r'(\d){3,5}?') # ? here indicates a "non greedy" match
mo12 = digitRegex.search('123456') #return 12345
mo13 = digit2Regex.search('123456') #return 123
