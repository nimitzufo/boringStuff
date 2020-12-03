#!/usr/bin/env python3
# a program to find phones and email addresses on the clipboard
import pyperclip as pc
import re

#phone regex
phoneRegex = re.compile(r'''(
        (\d{2}|\(\d{2}\))?      #area code
        (\s|-|\.)?              #separator
        (\d{5})                 #first 5 numbers
        (\s|-|\.)?              #separator
        (\d{4})                 #last 4 digits
        )''', re.VERBOSE)

#email regex
emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+       #username
        @                       #@ symbol
        [a-zA-Z0-9.-]+          #domain name
        (\.[a-zA-Z]{2,4})       #top-level domain
        )''', re.VERBOSE)
        

#matches in clipboard text
text = str(pc.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

#copy results to clipboard
if len(matches) > 0:
    pc.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phones of emails were found')

