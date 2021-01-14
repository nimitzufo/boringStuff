#!/usr/bin/python3
import sys

def collatz(value):
	while value!=1:
		if (value%2 == 1):
			value*=3
			value+=1
			print(value)
		elif(value%2 == 0):
			value//=2
			print(value)
	
	sys.exit()		

def main():
	while True:
		try:
			print('Enter number: ')
			number = int(input())
			collatz(number)

		except ValueError:
			print('Invalid input, enter an integer')
			continue

if __name__ == '__main__':
	main()