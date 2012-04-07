import converters.base

class Converter(converters.base.Converter):
    self.subroutines = []
    
    def convert(self):
        # TODO: Loop through all functions and convert to subroutines
        for function in self.parser.children():
            pass
            
            
        # TODO: add a call to the main subroutine
        
class Subroutine():
    def __init__(self, code):
        self.code = code
        
    def format(self):
        '''Return asm formatted code.'''
        pass