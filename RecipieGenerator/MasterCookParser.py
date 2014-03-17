import re
def loadContent(filename):
	f = open(filename, 'r')
	f.readline()
	f.readline()
	name = f.readline().strip()
	f.readline()
	f.readline()
	servingSize = f.readline().split()[3]
	categories = ""
	l = f.readline()
	while not "Amount" in l:
		categories += l
		l = f.readline()
	f.readline()
	line  = f.readline()
	ingrediantsAndAmounts = dict()
	'''
	This is a pretty big assumption to this
	 If there is an ingrediant the dictionary is 
	 {Ingrediant : Amount} if there are three elements
	 {Ingrediant : Fraction of that Ingrediant} if there are 2
	 { Ingrediant : "To taste"
	'''
	#TODO: It Seems that some ingredants have preperation tags that are 
	#	   in the form Ingrediant -- prep.  Need to represent that.
	while not line.isspace():
		temp = [s.strip() for s in line.split('  ') if s.strip()]
		if(len(temp) == 3):
			ingrediantsAndAmounts[temp[2]] = temp[0]+temp[1]
		if(len(temp) == 2):
			ingrediantsAndAmounts[temp[1]] = temp[0]
		else:
			ingrediantsAndAmounts[temp[0]] = "To Taste"
		line = f.readline()
	directions = ""
	for line in f:
		directions += line
	directions = [s.strip().replace('\n', '').replace('  ', ' ') for s in directions.split('.') if s.strip()]
	categories = categories.strip('Categories: ')
	categories = [s.strip() for s in categories.split('  ') if s.strip()]
	print categories
	print name
	print servingSize
	print len(directions)
	print ingrediantsAndAmounts
loadContent('C:\\Users\\spurrme\\Documents\\testRecipie.txt')