# Coding For Product Assessment - Exercises 1 & 2
# Ngozi Inyama - Submitted June 18, 2017
# ver 1.1


#  Exercise 1

print "Exercise 1 Output"

def linkmkr1(link1):
	if len(link1["title"]) > 50:
		short = link1["title"][0:50] + "..."
	else:
		short = link1["title"]
	print "The link is: <a href=\"%s\">%s</a>" % (link1["url"], short)
	

rat = linkmkr1({'title': 'This is a really really long title that bees had to be made up for testing', 'url': 'example.com'})

print


# Exercise 2

print "Exercise 2 Output"

def linkmkr2(link2):
	for x in link2:
		linkmkr1(x)

mouse = [
		{'title': 'This is a really really long title that had to be made up for testing', 'url': 'example.com'},
		{'title': 'Google', 'url': 'google.com'}, 
		{'title': 'Github', 'url': 'github.com'}
		]
		

gopher = linkmkr2(mouse)