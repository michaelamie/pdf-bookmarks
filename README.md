#pdf-bookmarks.py

is a *super-mega-ultra* **opinionated**™ piece of software that connects a few convenient and useful Python objects (designed by somebody else) in a highly-obvious and simplistic way that involved almost no effort whatsoever on my part to acheive a practical goal that I needed satisfied for a case where having a 1 GB application bundle floating around just to make a couple of lousy PDF bookmarks was complete and total overkill. I am so great; my genius is unsurpassed. It's very good.

###Clicky-clacky. Enter. Wow.

I spent more time marketing this than coding it. But, look: my marketing is almost as good as [Apple®](http://www.apple.com)!

###How To use it (like the champion you undoubtedly are):

Make a JSON list of lists of the form:

	[
		["Chapter 1: I am awesome", 1],
		["Chapter 2: Why I am the best person ever", 37],
		["Chapter 3: In which I rule the entire universe", 87]
	]
	
Now run the command:

	python pdf-bookmarks.py input.pdf boomarks.json n

Where n is some offset value that probably maps the first demarcated page to some actual page in the pdf document.