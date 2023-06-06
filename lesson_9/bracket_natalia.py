longread = input('Tell me your story \n> ')

for bracket in longread:
	open_bracket = longread.find('(')
	close_bracket = longread.find(')', open_bracket)
	longread = longread.replace(longread[open_bracket:close_bracket + 1], '')
print(f'In short, {longread}')