import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '870', 'Valencia', 'St.']

#check if cmd arg were passed, grab if they were
if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])

else:
    address = pyperclip.paste()

# go to websiste https://www.google.com/maps/place/<Address>
webbrowser.open('https://www.google.com/maps/place/' + address)

