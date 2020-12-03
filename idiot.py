#!/usr/bin/env python3 
import pyinputplus as pyip

while True:
    prompt = 'Do you want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break

print('Thanks, have a nice day')

while True:
    prompt = '¿Le gustaría saber como mantener a un idiota ocupado durante horas?\n'
    response = pyip.inputYesNo(prompt, yesVal='si', noVal='no')
    if response == 'no':
        break
print('Gracias, buen día')    
