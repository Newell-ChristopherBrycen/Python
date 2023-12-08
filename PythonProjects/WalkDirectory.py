import os

for folderName, subfolders, filenames in os.walk('c:\\delicious'):
    #print('The folder is: ' + folderName)
    #print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    #print('The filenames in ' + folderName + ' are: ' + str(filenames))
    #print()


# you can then loop to delete or rename a specific directory name pattern or a file type
    for subfolder in subfolders:
        if 'waffles' in subfolder:
            #os.rmdir(subfolder)
            print('rmdir on ' + subfolder)

    for file in filenames:
        if file.endswith('.txt'):
            #shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))
            print('create backup of ' + os.path.join(folderName, file))
