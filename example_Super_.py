class SimpleClass():
    
    def __init__(self,str_input):
        print("SIMPLE"+str_input)

class ExtendedClass(SimpleClass):
    
    def __init__(self):
        print('EXTENDED')

s = ExtendedClass()
