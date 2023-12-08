import re

namesRegex = re.compile(r'Agent \w+')
text = 'Agent Alice gave the secret documents to Agent Bob.'

print(namesRegex.findall(text)) #['Agent Alice', 'Agent Bob']

print(namesRegex.sub('REDACTED', text)) # REDACTED gave the secret documents to REDACTED.

namesRegex = re.compile(r'Agent (\w)\w*') # this identified the first character as its own group
print(namesRegex.findall(text)) # ['A', 'B']
print(namesRegex.sub(r'Agent \1****', text)) #Agent A**** gave the secret documents to Agent B****.



phoneRegex = re.compile(r'''
(\d\d\d-)  |    # AREA CODE WITHOUT PARENS, WITH DASH -OR-
(\(\d\d\d\) )   # AREA CODE W/ PARENS AND NO DASH
\d\d\d          # first 3 digits
-               # second dash
\d\d\d\d        # last 4 digits
\sx\d{2,4}      # a possible extension like x1234
''', re.VERBOSE | re.DOTALL | re.I)  # defines a multi line regex with '''
                                     # multiple expresion arguments with the | bitwise operator
