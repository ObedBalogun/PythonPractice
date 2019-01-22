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
        colors.append(colors)

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


