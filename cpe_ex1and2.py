# Coding For Product Assessment - Exercises 1 & 2
# Ngozi Inyama - Submitted June 18, 2017
# ver 1.0


#  Exercise 1

print "Exercise 1 Output"

def linkmkr1(title, link):
	if len(title) > 50:
		short = title[0:50] + "..."
	else:
		short = title
	print "The link is: <a href=\"%s\">%s</a>" % (link, short)
	

rat = linkmkr1("this is a really really long title that had to be made up for testing","example.com")


print

# Exercise 2

print "Exercise 2 Output"

def linkmkr2(link2):
	if len(link2["title"]) > 50:
		short = link2["title"][0:50] + "..."
	else:
		short = link2["title"]
	print "The link is: <a href=\"%s\">%s</a>" % (link2["url"], short)

mouse = [
		{'title': "This is a really really long title that had to be made up for testing", 'url': 'example.com'}, 
		{'title': 'Google', 'url': 'google.com'},
		{'title': 'Github', 'url': 'github.com'}
		]

for x in mouse:
	linkmkr2(x)
