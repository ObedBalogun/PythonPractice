'''
Identifiers

\d - any number
\D - anything but a number
\s - space
\S - anything but space
\w - any character
\W - anything but a character
. - any character except a newline
\b - the white space around
\. - period

Modifiers
(1,3) - we're expecting 1-3
+ - Match 1 or more
? - Match 0 or 1
* - Match 0 or more
$ - match the end of a string
^ - matching the beginning of a string
| - either or
[] - range of "variance" [A-Za-z], [1-5a-qA-Z]
{x} - expecting "x" amount

White Space Characters:
\n - new line
\s - space
\t - tab
\e - escape
\f - form feed
\r - return
'''

import re
example_string = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
'''
ages = re.findall(r'\d{1,3}', example_string)
names = re.findall(r'[A-Z][a-z]*', example_string)

print(ages)
print(names)

ageDict = {}
x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1

print(ageDict)