import re
'''
beginsWithHelloRegex = re.compile(r'^Hello')
endsWithHelloRegex = re.compile(r'Hello$')
allDigitsRegex = re.compile(r'^Hello$')

text = 'Hello there!'
text2 = 'I said Hello'
text3 = 'Hello'

print(beginsWithHelloRegex.search(text))
print(beginsWithHelloRegex.search(text2))
print(beginsWithHelloRegex.search(text3))
print('')
print(endsWithHelloRegex.search(text))
print(endsWithHelloRegex.search(text2))
print(endsWithHelloRegex.search(text3))
print('')
print(allDigitsRegex.search(text))
print(allDigitsRegex.search(text2))
print(allDigitsRegex.search(text3))


# another Example searching '.'

atRegex = re.compile(r'.at')
catText = 'The cat in the hat sat on the flat mat.'
print(atRegex.findall(catText))

# dotstar regex

nameRegex =   re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Al Last Name: Sweigart'))

serve = '<To serve humans> for dinner.>'

nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))
greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))

'''


prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'

print(prime)
      
dotStar = re.compile(r'.*') #reads all single line
print(dotStar.search(prime))

dotStar = re.compile(r'.*', re.DOTALL) # reads all
print(dotStar.search(prime))


vowelRegex = re.compile(r'[aeiou]') # only lowercase
vowelRegex = re.compile(r'[aeiou]', re.I) #Ignore case sensitive

