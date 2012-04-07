'''Handle the parsing of C code and store it in a Paser object.'''
import pycparser

class Parser():
    '''Parse the C code to an AST with pycparser and provide methods to
    access the code for the asm conversion process.
    '''
    
    def __init__(self, filename):
        self.filename = filename
        fileobj = open(filename)
        self.code = fileobj.read()
        fileobj.close()
        
        self.parser = pycparser.CParser()
        self.ast = self.parser.parse(self.code, filename)
        
    def children(self):
        return self.ast.children()
        
    def get_compound(self):
        '''Get the Compound section of the pycparser output.'''
        # WARNING: this code has not been tested!!!
        return self.ast.children()[0][1].children()[1][1]
        