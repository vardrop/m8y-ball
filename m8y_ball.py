from random import choice
import argparse
from json import loads
from glob import glob

parser = argparse.ArgumentParser(description='The classical magic 8-ball will now answer your questions.')
group = parser.add_mutually_exclusive_group(required=False) 
group.add_argument('input', nargs='?', help='predefined type')
group.add_argument('-i', type=argparse.FileType('r'), help='input file (txt)')
group.add_argument('-l', '--list', action='store_true', help='list all predefined types')
args = parser.parse_args()

positive = [
	'It is certain',
	'It is decidedly so',
	'Without a doubt',
	'Yes definitely',
	'You may rely on it',
	'As I see it, yes',
	'Most likely',
	'Outlook good',
	'Yes',
	'Signs point to yes'
]

ncommit = [
	'Reply hazy try again',
	'Ask again later',
	'Better not tell you now',
	'Cannot predict now',
	'Concentrate and ask again'
]
	
negativ = [
	'Don\'t count on it',
	'My reply is no',
	'My sources say no',
	'Outlook not so good',
	'Very doubtful'
]

answers = [positive, ncommit, negativ]

def listt():
	pre = glob('answer_*')
	pra = []
	for x in pre:
		pra.append(x.split('_',1)[1])
	return pra

def answt(pre):
	alist = []
	with open('answer_' + pre) as file:
		for line in file:
			alist.append(line.rstrip())
		answer = choice(alist)
	return answer

def answf(file):
	alist = []
	for line in file:
		alist.append(line.rstrip())
	answer = choice(alist)
	return answer

def answer():
	alist = []
	mood = choice(answers)
	answer = choice(mood)
	return answer

if __name__ == "__main__":
	if args.list:
		for x in listt():
			print(x)
	if args.input is not None:
		print(answt(args.input))
	if args.i is not None:
		print(answf(args.i))
	if not args.list and args.input is None and args.i is None:
		answer = answer()
		print(answer)