#Math
#math operators are +, -, /, *
a = 3 + 2
b = 3 - 2
c = 3/2
d = 3 * 2

#Print Function
print('This and the following are examples using the print function')
print('The value of 3 plus two is ', a)
print('The value of 3 minus two is ', b)
print('The value of 3 divided by two is ', c)
print('The value of 3 multiplied by two is ', d)
''' You can't use the '+' as a means of concatenation between an integer and
a string  '''

#Variables
exampleVar = print('This is a camel typed variable')
example_var = print('This is the accepted variable naming convention')
e,f = (3,5) #Variable Unpacking
print(e)
print(f)

#While Loop
#commonly used as a form of counter
condition = 1
while condition < 10:
    print(condition)
    condition += 1
#1,2,3,4,5,6,7,8,9


#For Loop
exampleList = [1,2,3,4,5,6,7,8,6,5,4,3,2]
for eachNumber in exampleList:
    print(eachNumber)

for x in range(1,11):
    print(x)
#1-10

#If Statement
g = 5
h = 8
i = 5
if g > h:
    print('g is greater than h') #won't run because of a false condition
if i < h > g:
    print('h is greater than i and greater than g')
if i <= g:
    print('i is less than or equal to g')

#if-else
if g > h:
    print('g is greater than h')
else:
    print('g is not greater than y')


#elif statement
if g < h:
    print('g is less than h')
elif g > i:
    print('g is greater than y')
else:
    print('if and elif never ran')


#Functions
def example():
    print('Basic Function')
    x = 3 + 8
    print(x)

example() #this calls the function and causes it to execute
def simple_addition(num1,num2):
    answer = num1 + num2
    print('num1 is', num1)
    print(answer)
simple_addition(5,3)  #calls the function and passes parameters 3 and 5 into it

#default parameters
def simple(num1, num2=5):
    print(num1,num2)

simple(2) #num2 is 5 by default


#global variables
x=6
def exmple():
    global x #defines x an a global variable
    print(x)
    # 'return' can also be used to make a variable globally accessible

#Writing and appending to a file

text = 'Sample Text to Save \n New line'
saveFile = open('exampleFile.txt','w')
saveFile.write(text)
saveFile.close()

appendMe = '\n New bit of information'
appendFile= open('exampleFile.txt', 'a')
appendFile.write(appendFile)
appendFile.close()

#Reading from a file
readMe = open('exampleFile.txt', 'r').read()
print(readMe)
#to read line by line you call .readlines() instead of read()

#Classes
class calculator:
    def addition(x,y):
        added = x + y
        print(added)
    def subtraction(x,y):
        sub = x - y
        print(sub)
    def multiplication(x,y):
        mult = x * y
        print(mult)
    def division(x,y):
        div = x / y
        print(div)

calculator.multiplication(3,5)
#class      #method      #arguments
#if __name__=='__main__': returns true if module being run is the main file

#Taking user input
name = input('What is your name? ')
print('Hello',name)
########################################################################################################################

#Math Functions
import statistics as s
example_list = [1,1,4,2,1,4,5,8,3,2,5,7,4,3]
example_list.sort() #sorts out the list
example_tuples = (1,2,4,4,9)
mean = s.mean(example_list)
median = s.median(example_list)
stdev = s.stdev(example_list)
var = s.variance(example_list)
example_list.insert(2,99)
example_list.remove(example_list[3])

#Importing third party librarys
import example_mod #example_mod was created and saved in the same
#directory
example_mod.ex('Test')


#multi-dimensional lists
dimensional_list = [
    [5,6],[6,7],[7,2],[2,5]
]
print(dimensional_list[1][0]) #prints out 6



