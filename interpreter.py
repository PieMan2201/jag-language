from sys import argv
import os
from time import sleep
from urllib2 import urlopen
from random import choice, randint
#Jag (Jag Allows Greatness) is a programming language made in Python.
#It is very simple, and it uses .jag files to store programs.
#The syntax is designed to look like English and can be understood easily.
#Created by Ishan Kamat in 2014

#TODO: 
#	Add lists (data type, add/remove, indexes)
#	Add errors (Syntax, Indentation, etc.)
#	Scan the code before running it!

#Info
version = '1.9'
status = 'alpha'
acronym_def = "Jag Allows Greatness"
year = '2014'
creators = [
	'Ishan Kamat',
	'Dhilan Lahoti'
]

def options():
	file = open("jag.conf")
	lines = file.read().split("\r\n")
	for line in lines:
		if "outp" in line:
			outp_setting = int(line[-1:])
		elif "line" in line:
			line_setting = int(line[-1:])
		elif "vars" in line:
			vars_setting = int(line[-1:])
		elif "cler" in line:
			cler_setting = int(line[-1:])
	return outp_setting, line_setting, vars_setting, cler_setting
outp_setting, line_setting, vars_setting, cler_setting = options()
#print options()
	
#Updates
def find_updates(url):
	update = urlopen(url)
	up_list = update.read().split()
	if float(up_list[0]) > float(version):
		print "\n----\nUPDATE AVAILABLE: version %s (Download @ %s).\n----\n" % (up_list[0], up_list[1])
		choice = raw_input("Would you like to download and install this update? [y/n]: ")
		sleep(2)

def check_updates():
	try:
		find_updates("http://98.198.233.69:8079")
	except:
		try:
			find_updates("http://192.168.1.126")
		except:
			pass

#check_updates()

commands = [
	'set ',
	'if ',
	'while ',
	'end if',
	'speak ',
	'end loop',
	'pause',
	'clear',
	'sleep ',
	'break loop',
	'stop'
]

set_commands = [
	'record ',
	' uppercase',
	' lowercase',
	' number',
	' string',
	'choose ',
	'open ',
	'append ',
	'remove '
]

comparisons = [
	' equals ',
	' does not equal ',
	' is greater than ',
	' is less than ',
]

operators = [' + ',' - ',' * ',' / ',' % ']


variables = {}
in_compare = False
tab_count = 0
line_counter = 0
just_looped = False
no_comparisons = False
should_break = False

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def list_check(line):
	if "[" in line and "]" in line and (line[-1:] == "]" if "set " in line else True):
		start_index = line.index("[")
		end_index = line.index("]")
#		print line[start_index + 1:end_index]
		try:
			index = int(check_type(line[start_index + 1:end_index]))
		except:
#			print "boo"
			return line
		wordlist = []
		for char in reversed(line[:start_index]):
			if char != " ":
				wordlist.append(char)
				new_start_index = line.index(char)
			else:
				break
		listname = "".join(wordlist)
		wordlist = []
		for char in reversed(listname):
			wordlist.append(char)
		listname = "".join(wordlist)
		actuallist = variables[listname]
		value = actuallist[index]
		#print value
#		print value
#		print line
#		print line[new_start_index:end_index + 1]
#		print line[end_index + 1:]
#		print line[:new_start_index]
		full_line = line[:new_start_index] + str(value) + line[end_index + 1:]
#		print full_line 
#		print len(full_line)
		return full_line
	else:
#		print "boo1"
		return line
	
def string_check(line):
#	print "Line: " + line
	found = 0
	for operator in operators:
		if operator in line and '"' + operator + '"' not in line:
			found = 1
			line_list = line.split(operator)
			break
	if not found:
#		print "BROKE 1"
		return line
	found = 0
	for char in line_list[0]:
		if char == '"':
			start_cut = line_list[0].index(char)
			for char in line_list[0][start_cut + 1:]:
				if char == '"':
					end_cut = line_list[0][start_cut + 1:].index(char) + start_cut + 1
					part1 = '"' + line_list[0][start_cut + 1:end_cut] + '"'
					remaining_line = line_list[0][:start_cut]
					found = 1
					break
			break
	if not found:
		part1 = line_list[0].split()[-1]
		remaining_line = " ".join(line_list[0].split()[:-1]) + " "
	part2 = line_list[1]
	part1 = check_type(part1)
	part2 = check_type(part2)
	string = True
	try:
		part1 + " "
		part2 + " "
	except:
		string = False
#		print "BROKE 2"
#		print part1, part2
	if not string:
		return line
	if operator == operators[0]:
		answer = '"' + part1 + part2 + '"'
#	print remaining_line + str(answer)
	return remaining_line + str(answer)

def math_check(line):
	found = 0
	for operator in operators:
		if operator in line:
			found = 1
			line_list = line.split(operator)
			break
	if not found:
		return line
	part2 = line_list[-1]
	part1 = line_list[0].split()[-1]
	remaining_line = " ".join(line_list[0].split()[:-1])
	part1 = check_type(part1)
	part2 = check_type(part2)
	num = True
	try:
		part1 + 1
		part2 + 1
	except:
		num = False
	if not num:
		return line
	if operator == operators[0]:
		answer = part1 + part2
	elif operator == operators[1]:
		answer = part1 - part2
	elif operator == operators[2]:
		answer = part1 * part2
	elif operator == operators[3]:
		answer = part1 / part2
	elif operator == operators[4]:
		answer = part1 % part2
	return remaining_line + " " + str(answer)

def check_type(term):
	global variables
	
	type = find_type(term)
	if type == 0:
		return term[1:-1]
	elif type == 1:
		return variables[term]
	elif type == 2:
		return float(term)
	else:
		return None

def find_type(term):
	global variables

	if term[0] == '"' and term[-1:] == '"':
		return 0
	elif term in variables.keys():
		return 1
	else:
		try:
			float(term)
			return 2
		except:
			pass
#	print term
	return None
def compare(term1,term2,comparison):
	term1,term2 = check_type(term1),check_type(term2)
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
#	print term1, term2
	check2 = check_type(term2)
	if "[" in term1 and "]" in term1:
		start_index = term1.index("[")
		end_index = term1.index("]")
		index = int(term1[start_index + 1:end_index])
		#print index
		listname = term1[:start_index]
		#print listname
		#print variables[listname][index]
		variables[listname][index] = '"' + str(check2) + '"'
		#print variables[listname][index]
		#raw_input()
	if check2 != None:
		variables[term1] = check2
		return 1
	else:
		if term2[:1] == "[" and term2[-1:] == "]":
			elements = term2[1:-1].split(', ')
			#print elements
			if elements != [""]:
				variables[term1] = elements
			else:
				variables[term1] = []
			return 1
		for command in set_commands:
			if command in term2:
#				print "CMD: " + command
#				print set_commands.index(command)
				if command == set_commands[0]:
					message = check_type(term2[7:])
					term2 = raw_input(str(message))
					term2 = check_type(term2)
				elif command == set_commands[1]:
					variable = term2.split()[0]
					variable = check_type(variable).upper()
					term2 = variable
				elif command == set_commands[2]:
					variable = term2.split()[0]
					variable = check_type(variable).lower()
					term2 = variable
				elif command == set_commands[4]:
#					print term2.split()
					variable = term2.split()[0]
					variable = str(check_type(variable))
					term2 = variable
#					print term2
				elif command == set_commands[3]:
					variable = term2.split()[0]
					variable = float(check_type(variable))
					term2 = variable
				elif command == set_commands[5]:
					bounds = term2[7:].split(' to ')
					term2 = float(randint(int(float(bounds[0])), int(float(bounds[1]))))
				elif command == set_commands[6]:
					filename = term2[5:]
					term2 = open(filename).read()
				elif command == set_commands[7]:
					listname = term2[7:]
					type = find_type(term1)
					#print type
					if type == 1:
						term1 = variables[term1]
						try:
							term1 + ""
							term1 = '"' + term1 + '"'
						except:
							term1 = check_type(str(term1))
					variables[listname].append(term1)
					#print variables[listname]
					return 1
				elif command == set_commands[8]:
					listname = term2[7:]
					type = find_type(term1)
					#print type
					if type == 1:
						term1 = variables[term1]
						try:
							term1 + ""
							term1 = '"' + term1 + '"'
						except:
							term1 = check_type(str(term1))
					variables[listname].remove(term1)
					return 1
				variables[term1] = term2
				break	

def while_loop(start, end, comparison_statement):
	global line_counter
	global in_compare
	global just_looped
	global no_comparisons
	global should_break
	
#	print start, end
	for comparison in comparisons:
		if comparison in comparison_statement:
			saved_comparison = comparison
			term1, term2 = comparison_statement.split(comparison)
			break
	compared = compare(term1,term2,saved_comparison)
	while compared:
		no_comparisons = False
		should_break = False
		line_counter = start
		add_to_counter = 0
		while line_counter < end:
			line_counter = start + add_to_counter
			main()
			if should_break:
				break
			if line_counter == len(lines):
				break
			add_to_counter = line_counter - start
			add_to_counter += 1
		if not no_comparisons:
			compared = compare(term1,term2,saved_comparison)
		else:
			compared = False
		should_break = False
		no_comparisons = False
		if line_counter == len(lines):
			break
	else:
		line_counter = end
		just_looped = True

def check_line(line):
	global in_compare
	global tab_count
	global no_comparisons
	global should_break
	global line_counter
	global variables
	
	#print variables
	tab_count = 0
	true_line = line
	line = list_check(line)
	line = string_check(line)
	line = math_check(line)
	#print "Current line: " + line
	while "\t" == line[0]:
		line = line[1:]
		tab_count += 1
	if commands[0] == line[:4]:
		thinglist = line[4:].split(' to ')
		term1 = thinglist[0]
		thinglist.remove(term1)
		term2 = " to ".join(thinglist)
		set(term1, term2)
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
		start_index = line_counter + 1
#		for line in lines[start_index:]:
#			print line
		for line in lines[start_index:]:
			if "\t" * tab_count + commands[5] == line:
				end_index = lines[start_index:].index(line) + start_index
		comparison = old_line[6:]
#		print old_line
		while_loop(start_index, end_index, comparison)
	elif commands[4] == line[:6]:
		prefix = ""
		suffix = ""
		if outp_setting: 
			prefix = "Output: "
		if line_setting:
			suffix = " (Line %s)" % str(line_counter + 1)
		print prefix + str(check_type(line[6:])) + suffix
	elif commands[6] == line[:5]:
		raw_input('Press enter to continue . . .')
	elif commands[7] == line[:5]:
		if cler_setting:
			print "Clearing screen..."
			sleep(0.75)
		clear()
	elif commands[8] == line[:6]:
		sleep_interval = float(line[6:])
		sleep(sleep_interval)
	elif commands[9] == line[:10]:
		no_comparisons = True
		should_break = True
	elif commands[10] == line[:4]:
		line_counter = len(lines)

#Credits section
def run_credits():
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
	global line_counter, variables, in_compare, tab_count
	
	try:
		line = lines[line_counter]
		if "haltcode" in line:
			go_crazy()
			raise IndexError
	except IndexError:
		print "\nReached end (Line %s). Quitting..." % str(line_counter + 1)
		if vars_setting:
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