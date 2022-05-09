class SimpleClass():
    
    def __init__(self,str_input):
        print("SIMPLE"+str_input)

class ExtendedClass(SimpleClass):
    
    def __init__(self):
        print('EXTENDED\n')

s = ExtendedClass()

class ExtendedClass(SimpleClass):
    
    def __init__(self):
        
        super().__init__(" My String")
        print(f'EXTENDED')

s2 = ExtendedClass()
