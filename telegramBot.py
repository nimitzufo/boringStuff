
import telegram_send
import time, schedule, requests, random


def telegramBotSendtext(message):
	telegram_send.send(messages=[message])


def generateMessage():
	
	messageArray = [ 'lembra de tomar o remédio',
	'não esquece de tomar o remédio',
	'já tomou o remédio hoje?'
	]

	messageSelected = messageArray[random.randint(0, len(messageArray)-1)]
	messageToSend = f'Amor, {messageSelected}.\namo você bochechudinha :3'

	return messageToSend


def main():
	
	textMessage = generateMessage()
	telegramBotSendtext(textMessage)



if __name__ == '__main__':
	main()
	
