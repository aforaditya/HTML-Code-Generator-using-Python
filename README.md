# HTML-Code-Generator-using-Python

What if there is someone who just loves Python and is too arrogant to learn HTML ?
No worries, HTML Code Generator comes to the rescue.

You can create a HTML file without even coding in HTML .
All you need to know is basics of python.

This program treats every HTML element as an object.

Some functions of the program:


html = Element('html')      # to create an element (html element)  <br>
head = Element('head')      # creating another element <br>
html.add(head)              # adding the newly created head element inside the html element <br>
body = Element('body')      # creating body element <br>
html.add(body)
head.add(Element('title', 'My first website'))        # adding an element in head  with content 'My first website' <br>
h1 = Element('h1','This is a h1 heading')
inp = Element('input') <br>
inp.add_atr('placeholder','Enter your name') <br>
inp.add_atr('title','Enter your full name') <br>
body.add(h1) <br>
body.add(inp) <br>
btn = Element('button','Submit') <br>
body.add(btn) <br>

script = Element('script', 'alert("hello")')   <br>  
body.add(script) <br>

#Element.display(html) <br>
Element.create_file(html)    # final method to render html file as output
 
