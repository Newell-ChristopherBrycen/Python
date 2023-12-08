helloFile = open('C:\\Users\\bryne\\Documents\\Test.txt') # open the file in read-only mode

helloFile.read()
helloFile.close()
helloFile.open()

helloFile = open('C:\\Users\\bryne\\Documents\\Test.txt', 'w') #overwriting the file
helloFile = open('C:\\Users\\bryne\\Documents\\Test.txt', 'a') # adding information to the end of the file

import shelve # Used to store data like a dictionary to reopen later

shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()


shelfFile = shelve.open('mydata')
shelfFile['cats'] # returns previous data
shelfFile.close()

