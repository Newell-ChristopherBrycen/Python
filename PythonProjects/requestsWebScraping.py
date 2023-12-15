import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
badRes = requests.get('https://automatetheboringstuff.com/kjsislgnieon')
print(res.status_code) # 200 means success, 404 means not found


print(len(res.text))

print(res.text[:500])

res.raise_for_status() #returns nothing, successful
#badRes.raise_for_status() # returns detailed 404 Client error

#------ res.iter_content()

playFile = open('RomeoAndJuliet.txt', 'wb') #opened in write binary mode (wb)

for chunk in res.iter_content(100000):
    print(playFile.write(chunk)) #shares the number of bytes on each chunk

playFile.close()
