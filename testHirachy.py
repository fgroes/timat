class Element(object):
    
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        
    def addChild(self, child):
        child.parent = self
        self.children.append(child)
    
    def __str__(self):
        return self.name
        
        
def findElementsBase(elements):
    elementsLeft = elements[:]
    elementsBase = []
    while len(elementsLeft) > 0:
        element = elementsLeft.pop(0)
        if len(element.children) > 0:
            elementsLeft += element.children
        else:
            elementsBase.append(element)
    return elementsBase
    
        
elements = [Element('1'), Element('2'), Element('3')]
elements[0].addChild(Element('4'))
elements[0].addChild(Element('5'))
elements[0].children[0].addChild(Element('9'))
elements[0].children[0].addChild(Element('10'))
elements[2].addChild(Element('6'))
elements[2].addChild(Element('7'))
elements[2].addChild(Element('8'))
elements[2].children[2].addChild(Element('11'))
base = findElementsBase(elements)
for e in base:
    print(e)