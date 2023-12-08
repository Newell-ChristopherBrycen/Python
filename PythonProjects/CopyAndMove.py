import shutil

shutil.copy('c:\\spam.txt', 'c:\\delicious')
# Returns 'c:\\delicious\\spam.txt', this is where the file was copied to

shutil.copy('c:\\spam.txt', 'c:\\delicious\\spamspamspam.txt')
# returns 'c:\\delicious\\spamspamspam.txt', indicating file was copied and renamed as specified


shutil.copytree('c:\\delicious', 'c:\\delicious_backup')
# returns c:\\delicious_backup, this is the new copied folder

shutil.move('c:\\spam.txt', 'c:\\delicious\\walnut')
# returns 'c:\\delicious\\walnut\\spam.txt', indicating the move successful

shutil.move('c:\\spam.txt', 'c:\\eggs.txt')
# returns c:\\eggs.txt, indicating file rename successful
