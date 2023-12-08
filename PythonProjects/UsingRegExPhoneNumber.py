import re

message = 'Call me at 555-555-5555 tomorrow, or at 555-555-5556 the day after.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)

print(mo.group())
print(phoneNumRegex.findall('Call me at 555-555-5555 tomorrow, or at 555-555-5556 the day after.'))
      
