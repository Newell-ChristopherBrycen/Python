import os
'''spam = os.path.join('folder1','folder2','folder3','file.png')


os.sep #returns '\\'

os.getcwd() # retuns current working directory

os.chdir('path') #changes directory to path specified
'''
# ..\ indicates a relative path to my current parent directory
# .\ indicates the relative path to my current directory


# C:\bacon\fizz\eggs\spam.txt
#           ^
#           ^ this is my directory which can be identified by .\
#           my parent directory is C:\bacon and can be identified by ..\


#        I could get to the eggs folder by using either:
#           os.chdir('C:\\bacon\\fizz\\eggs')
#               OR
#           os.chdir('.\eggs')


os.path.abspath('spam.txt')  # returns the absolute path of this file if within your current directory
#     this would be C:\\bacon\\fizz\\eggs\\spam.txt

os.path.isabs('C:\\bacon\\fizz\\eggs\\spam.txt') # only true if the path supplied is an aboslute path

os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1') # shows relative path for arg2 to reach arg1
                # example would return 'folder2\\spam.png'


os.path.dirname('c:\\folder1\\folder2\\spam.png')
                # returns 'c:\\folder1\\folder2' to identify the directory names

os.path.basename('c:\\folder1\\folder2\\spam.png')
                # returns spam.png to identify the base file name
                # can also idenfity the final file folder mentioned if not file name exists


os.path.exists('c:\\folder1\\folder2\\spam.png') # is this real?

os.path.isfile('c:\\folder1\\folder2\\spam.png') # true, this is a file

os.path.isdir('c:\\folder1\\folder2\\spam.png') # false, this is not the directory

os.path.getsize('c:\\folder1\\folder2\\spam.png') # returns size of file in bytes

os.listdir('c:\\folder1\\folder2') # returns what files are within this foldertotalSize = 0


####-------------------- FOLDER DIRECTORY SIZE -------------------###

totalSize = 0

for filename in os.listdir('C:\\Users\\bryne\\Documents\\GitHub\\Python\\PythonProjects'):
    if not os.path.isfile(os.path.join('C:\\Users\\bryne\\Documents\\GitHub\\Python\\PythonProjects', filename)):
            continue
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Users\\bryne\\Documents\\GitHub\\Python\\PythonProjects', filename))

    
# os.makedirs('c:\\bacon\\fizz\\eggs\\spam2') # will create the spam 2 folder
