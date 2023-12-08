def isPhoneNumber(text):
    if len(text) != 12:
        return False # not a phone number size
    
    for i in range(0,3):
        if not text[i].isdecimal():
            return False #no area code
        if text[3] != '-':
            return False # not a dash

    for i in range(4,7):
        if not text[i].isdecimal():
            return False #missing first 3 digits
        if text[7] != '-':
            return False # not a dash
        
    for i in range(8,12):
        if not text[i].isdecimal():
            return False #missing last 4 digits

    return True



# --------------------

message = 'Call me at 555-555-5555 tomorrow, or at 555-555-5556 the day after.'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')
