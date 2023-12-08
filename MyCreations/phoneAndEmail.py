#! python3
import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 580-555-1234, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(
((\d\d\d)|(\(\d\d\d\)))?                                  # area code (optional)
(\s|-)                                                    # first separator
\d\d\d                                                    # first 3 digits
-                                                         # separator
\d\d\d\d                                                  # last 4 digits
(((ext(\.)?\s)|x)                                          # extension word-part (optional)
(\d{2,5}))?                                               # extension number part (optional)
)
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@something.com

[a-zA-z0-9_.+]+                                           # name part
@                                                         # @ symbol
[a-zA-z0-9_.+]+                                           # domain name part


''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the data from this text
extractedPhone = phoneRegex.findall(text) # provides something like [('678-560-3485', '678', '678', '', '-', '', '', '', '', '')]
extractedEmail = emailRegex.findall(text) # provides the email we want

allPhoneNumbers = [] # this is to organize the data received from the Regex Find All to just the first value [0]
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])



#TODO: copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)

pyperclip.copy(results)
