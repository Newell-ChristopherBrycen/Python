import os

os.getcwd()

os.rmdir('c:\\delicious') # can remove directory if empty

import shutil
#!!!!careful!!!!!
shutil.rmtree('c:\\delicious') # removes the file folder and its items
#!!!!careful!!!!!



import send2trash
send2trash.send2trash('c:\\delicious') # sends file to trash rather than delete forever



