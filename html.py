import random

random_file_number = random.randint(10000,99999)
doc = ''

class Element(object):
    

    def __init__(self, tag, content=''):
        
        self.tag = tag
        self.content = content
        self.attributes = []
        self.children = []

    def add_atr(self, name, value=''):
        
        self.attributes.append([name,value])
        
    def add(self, child):
        
        self.children.append(child)


    
    @staticmethod
    def create_doc(ele, lvl=0):

            global doc

            doc+= '\n'
            doc+= '{0}<{1}'.format('\t'*lvl,ele.tag) 
        
            for attr in ele.attributes:
                doc+=' '
                doc+= '{}="{}"'.format(attr[0] , attr[1])
            doc+='>\n'

        
            if not ele.content == '':
                doc+= '{0}{1}\n'.format('\t'*lvl,ele.content)
            for child in ele.children:
                Element.create_doc(child, lvl+1)
            
            doc+= '{0}</{1}>\n'.format('\t'*lvl,ele.tag)
            doc+= '\n'

            return doc

    @staticmethod   
    def create_file(ele):

        with open('my_html_file.html','w') as file:
            if doc=='':
                print(Element.create_doc(ele), file=file)
            else:
                print(doc, file=file)
        print('HTML file created successfully.')

    @staticmethod
    def display(ele):
        if doc=='':
            print(Element.create_doc(ele))
        else:
            print(doc)
        

    
            
     

html = Element('html')
head = Element('head')
html.add(head)
body = Element('body')
html.add(body)
head.add(Element('title', 'My first website'))
h1 = Element('h1','This is a h1 heading')
inp = Element('input')
inp.add_atr('placeholder','Enter your name')
inp.add_atr('title','Enter your full name')
body.add(h1)
body.add(inp)
btn = Element('button','Submit')
body.add(btn)

script = Element('script', 'alert("hello")')
body.add(script) 

#Element.display(html)
Element.create_file(html)


