print('Enter a name.') #Ask for Name
name = input()
if name != '':
    print('Thank you for enterning a name.')
else:
    print('You did not enter a name.')


print('Enter an age.') #Ask for Age
age = int(input())
if age:
    print('Thank you for enterning an age.')
else:
    print('You did not enter an age.')

#Run Identification Program
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
