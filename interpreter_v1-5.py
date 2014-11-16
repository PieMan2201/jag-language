from sys import argv
import os
from time import sleep
from urllib2 import urlopen
from random import choice, randrange
#Jag (Jag Allows Greatness) is a programming language made in Python.
#It is very simple, and it uses .jag files to store programs.
#The syntax is designed to look like English and can be understood easily.
#Created by Ishan Kamat in 2014

#TODO: 
#	Add lists (data type, add/remove, indexes)
#	Add errors (Syntax, Indentation, etc.)
#	Scan the code before running it!

#Info
version = '1.5'
status = 'alpha'
acronym_def = "Jag Allows Greatness"
year = '2014'
creators = [
	'Ishan Kamat',
	'Dhilan Lahoti'
]

#Updates
try:
	update = urlopen('http://98.198.233.69:8079')
	up_list = update.read().split()
	if up_list[0] != version:
		print "\n----\nUPDATE AVAILABLE: version %s (Download @ %s).\n----\n" % (up_list[0], up_list[1])
except:
	try:
		update = urlopen('http://192.168.1.126')
		up_list = update.read().split()
		if up_list[0] != version:
			print "\n----\nUPDATE AVAILABLE: version %s (Download @ %s).\n----\n" % (up_list[0], up_list[1])
	except:
		pass

commands = [
	'set ',
	'if ',
	'while ',
	'end if',
	'speak ',
	'record ',
	'end loop',
	'pause',
	'clear',
	'sleep ',
	'make ',
	'choose '
]

comparisons = [
	' equals ',
	' does not equal ',
	' is greater than ',
	' is less than ',
]

operators = ['+','-','*','/']

conversions = [
	'uppercase',
	'lowercase',
	'number',
	'string'
]

variables = {}
in_compare = False
tab_count = 0
bad_dexes = []
line_counter = 0
just_looped = False

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def math_check(line):
	line_list = line.split()
	found = 0
	for operator in operators:
		if operator in line_list:
			found = 1
			operator_index = line_list.index(operator)
			break
	if not found:
		return line
	part1 = line_list[operator_index - 1]
	part2 = line_list[operator_index + 1]
	remaining_line = line_list[:operator_index - 1]
	remaining_line = " ".join(remaining_line)
	check1 = check_var_or_string(part1)
	check2 = check_var_or_string(part2)
	if check1 == 0:
		part1 = variables[part1]
	else:
		part1 = float(part1)
	if check2 == 0:
		part2 = variables[part2]
	else:
		part2 = float(part2)
	if operator == operators[0]:
		answer = part1 + part2
	elif operator == operators[1]:
		answer = part1 - part2
	elif operator == operators[2]:
		answer = part1 * part2
	elif operator == operators[3]:
		answer = part1 / part2
	return remaining_line + " " + str(answer)

def check_var_or_string(term):
	global variables
	
	if term[0] == '"' and term[-1:] == '"':
		return 1
	elif term in variables.keys():
		return 0
	else:
		try:
			float(term)
			return 2
		except:
			pass

def compare(term1,term2,comparison):
	
	check1,check2 = check_var_or_string(term1),check_var_or_string(term2)
	
	if check1 == 0:
		term1 = variables[term1]
	elif check1 == 1:
		term1 = term1[1:-1]
	elif check1 == 2:
		term1 = float(term1)
	if check2 == 0:
		term2 = variables[term2]
	elif check2 == 1:
		term2 = term2[1:-1]
	elif check2 == 2:
		term2 = float(term2)

	if comparison == comparisons[0]:
		if term1 == term2:
			return 1
		else:
			return 0
	elif comparison == comparisons[1]:
		if term1 != term2:
			return 1
		else:
			return 0
	elif comparison == comparisons[2]:
		if term1 > term2:
			return 1
		else:
			return 0
	elif comparison == comparisons[3]:
		if term1 < term2:
			return 1
		else:
			return 0

def set(term1,term2):

	check2 = check_var_or_string(term2)
	if check2 == 0:
		variables[term1] = variables[term2]
	elif check2 == 1:
		variables[term1] = term2[1:-1]
	elif check2 == 2:
		variables[term1] = float(term2)
	else:
		print "UNRECOGNIZED: " + term2

def while_loop(start, end, comparison_statement):
	global line_counter
	global in_compare
	global just_looped
	
	for comparison in comparisons:
		if comparison in comparison_statement:
			saved_comparison = comparison
			term1, term2 = comparison_statement.split(comparison)
			break
	compared = compare(term1,term2,saved_comparison)
	while compared:
		line_counter = start
		add_to_counter = 0
		while line_counter < end:
			line_counter = start + add_to_counter
			main()
			add_to_counter = line_counter - start
			add_to_counter += 1
		compared = compare(term1,term2,saved_comparison)
	else:
		line_counter = end + 1
		just_looped = True

def make(term1, term2, conversion):
	global conversions
	
	check = check_var_or_string(term2)
	if check == 0:
		term2 = variables[term2]
	elif check == 1:
		term2 = term2[1:-1]
	elif check == 2:
		term2 = float(term2)
	
	if conversion == conversions[0]:
		variables[term1] = term2.upper()
	elif conversion == conversions[1]:
		variables[term1] = term2.lower()
	elif conversion == conversions[2]:
		variables[term1] = float(term2)
	elif conversion == conversions[2]:
		variables[term1] = str(term2)
#	print "new: " + str(variables[term1])
def check_line(line):
	global commands
	global comparisons
	global variables
	global lines
	global in_compare
	global tab_count
	global bad_dexes

	tab_count = 0
	true_line = line
#	print "----"
#	print line
	line = math_check(line)
	while "\t" == line[0]:
		line = line[1:]
		tab_count += 1
#	print line
#	print "----"
	if commands[0] == line[:4]:
		term1, term2 = line[4:].split(' to ')
		set(term1,term2)

	elif commands[1] == line[:3]:
		compared = False
		newline = line[3:]
		for comparison in comparisons:
			if comparison in newline:
				compared = True
				term1, term2 = newline.split(comparison)
				t_or_f = compare(term1,term2,comparison)
				if not t_or_f:
					in_compare = True
		if not compared:
			print "UNCOMPARED: " + newline
			in_compare = True

	elif commands[2] == line[:6]:

		old_line = line
		
		for line in lines[lines.index("\t" * tab_count + line):]:
			if "\t" * tab_count + commands[6] == line:
				end_index = lines.index(line)
		start_index = lines.index(true_line) + 1
		comparison = old_line[6:]
		while_loop(start_index, end_index, comparison)
	elif commands[4] == line[:6]:
#		print "PRINTING " + line[6:]
#		print check_var_or_string(line[6:])
#		print variables
		if check_var_or_string(line[6:]) == 1:
			print "Output: " + str(line[7:-1]) + " (Line %s)" % str(line_counter + 1)
		elif check_var_or_string(line[6:]) == 0:
			print "Output: " + str(variables[line[6:]]) + " (Line %s)" % str(line_counter + 1)
		elif check_var_or_string(line[6:]) == 2:
			print "Output: " + str(line[6:]) + " (Line %s)" % str(line_counter + 1)
	elif commands[5] == line[:7]:
		params = line[7:].split(' to ')
		if len(params) == 1:
			message = ""
			term1 = line[7:]
		elif len(params) == 2:
			message = params[0]
			type = check_var_or_string(message)
			if type == 0:
				message = variables[message]
			elif type == 1:
				message = message[1:-1]
			elif type == 2:
				message = float(message)
			term1 = params[1]
		term2 = raw_input(str(message))
		if term2 != "":
			set(term1,term2)
	elif commands[7] == line[:5]:
		raw_input('Press enter to continue ')
	elif commands[8] == line[:5]:
		print "Clearing screen..."
		sleep(0.75)
		clear()
	elif commands[9] == line[:6]:
		sleep_interval = float(line[6:])
		sleep(sleep_interval)
	elif commands[10] == line[:5]:
		term1, remaining = line[5:].split(' be ')
		term2, conversion = remaining.split()
		make(term1, term2, conversion)
	elif commands[11] == line[:7]:
		num1, remaining = line[7:].split(' to ')
		num2, variable = remaining.split(' for ')
		variables[variable] = randrange(int(float(num1)),int(float(num2)))
#Credits section
def run_credits():
	global acronym_def, version, status, creators, year
	credit_lines = [
		' ',
		'Jag PROGRAMMING LANGUAGE',
		'(' + acronym_def + ')',
		' ',
		'Version %s (%s)' % (version, status),
		'Written in Python 2.7',
		' ',
		'Created by:'
	]	
	credit_lines += creators + [' ', year, ' ']

	length = 8
	while credit_lines != []:
		try:
			writing = ""
			counter = 0
			for line in credit_lines:
				writing += line + "\n"
				counter += 1
				if counter == length:
					break
			new_length = counter
			difference = length - new_length
			writing = "-------- \n" + writing + "\n" * difference + "-------- \n"
			clear()
			print writing
			sleep(1)
			credit_lines.pop(0)
		except:
			pass
	clear()
#End Credits section

try:
	file = open(argv[1])
except:
	if len(argv) == 1:
		print "Please provide a file!"
	else:
		print "Invalid file!"
	raise SystemExit
	
lines = file.read().split('\n')

if lines == ['']:
	print "It seems you've sent me an empty file. \nIf you send me an empty file, I'm supposed to play the credits. \nSo, here they are!"
	sleep(4)
	run_credits()
	raise SystemExit

def main():
	global lines, line_counter, variables, incompare, tab_count, commands, in_compare
	try:
		line = lines[line_counter]
		if "haltcode" in line:
			go_crazy()
			raise IndexError
	except IndexError:
		print "\nReached end (Line %s). Quitting..." % str(line_counter + 1)
		print "---- \nVARS: \n"
		for key in variables:
			print key + " : " + str(variables[key])
		print ""
		raise SystemExit
	if "%" != line[:3]:
		if not in_compare:
			check_line(line)
		elif ("\t" * tab_count) + commands[3] == line:
			in_compare = False

def go_crazy():
	file = open(argv[1], 'w')
	chars = ['!','@','#','$','%','^','&','*','(',')','+','=','_','-','|','\',','?','"','>','<','\n','\t']
	char_count = 0
	to_write = ""
	while char_count < 10**5:
		pick = choice(chars)
		to_write += pick
		char_count += 1
	file.write(to_write + "\n\n Shouldn't have used haltcode...")
	file.close()
	
while True:
	main()
	
	if not just_looped:
		line_counter += 1
	else:
		just_looped = False