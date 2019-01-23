#Handling comma separated variable files
import csv
with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        #items in csv files are stored as strings and as such can be accessed likewise
        date = row[0]
        color = row[3]
        dates.append(date)
        colors.append(color)
#Error handling using try and except
#Tries this block of code
try:
    whatColor = input('What color do you wish to know the date of?')
    #its generally good practise to test user input for authenticity
    if whatColor in colors:
        color_index = colors.index(whatColor)
        theDate = dates[color_index]
        print('The date of',whatColor,'is:',theDate)
    else:
        print('Input does not exist or is incorrect')
#Program breaks and executes the except block if the try block throws an exception
except Exception as e:
     print(e)
print("continuing")

#Multi-line print
print('''
This is
a
multi-line print

============
|    this  |
|    is    |
|    cool  |
============
''')

#Dictionaries (key, value pairs)
exDict = {'Jack':15, 'Bob':22, 'Alice':12, 'Kevin':17}
print(exDict['Alice']) #Print Value at index/Key 'Alice'
exDict['Tim'] = 14 #Add value 14 at key "Tim"
new_dict = {'Jack':[15,'blonde'], 'Bob':[22, 'black'], 'Alice':[12, 'red'],'Kevin':[17,'brown']}
print(new_dict['Jack'][1]) #blonde

#Using the 'os' built-in function
import os
import time
os.mkdir('newDir') #creates directory
time.sleep(2) #sets a delay
os.rename('newDir','newDir2')
time.sleep(3)
os.rmdir('newDir2') #removes directory
#Using urlLib
import urllib.request as url
import urllib.parse as par #for parsing data
# x = url.urlopen('http://pythonprogramming.net') #url to open
# values = {
#     's':'basic',
#     'submit':'search'
# }
# data = par.urlencode(values) #encode values as data to be posted
# data = data.encode('utf-8')
# req = url.Request(x,data)#Request() takes in two parameters, the url and the data to be parsed e.g google.com/?s=hey submit=there
# resp = url.urlopen(req)
# respData = resp.read() #read the data of the url and the parsed values

######This is how to bypass the google api using headers#########
try:
    url_link = 'https://www.google.com/search?q=test'
    headers = {} #headers contains information on you when you visit a website
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    req = url.Request(url_link, headers=headers)
    resp = url.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()

except Exception as e:
    print(str(e))