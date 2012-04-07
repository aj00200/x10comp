import pycparser
import converters.base

class Converter(converters.base.Converter):
    '''Convert the code accessed through the parser object into asm.'''
    def __init__(self, parser):
        super(Converter, self).__init__(parser)
        self.subroutines = {}
    
    def convert(self):
        '''Convert functions to asm subroutines and store them in a
        Subroutine object for later access.
        '''
        # TODO: Loop through all functions and convert to subroutines
        for function in self.parser.children():
            funcobj = function[1]
            name = funcobj.children()[0][1].children()[0][1].type.declname
            print('[*] Got function: %s' % name)
            asm = self.cfunc2asm(funcobj)
            
            subroutine = Subroutine(name, asm)
            
        # TODO: Place subroutines in the file
            
        # TODO: add a call to the main subroutine
        
    def cfunc2asm(self, function):
        '''Take a pycparser function as input and output the 0x10c asm.'''
        print(' [*] Inside function:')
        funcbody = function.children()[1][1]
        funcbody_instructions = funcbody.children()
        funcbody.show()
        
        for instruction in funcbody_instructions:
            instr = instruction[1]
            # print(instr)
            if isinstance(instr, pycparser.c_ast.Return):
                print('  [*] Got return instruction')
                
    def cinstr2asm(self, instruction):
        '''Convert a single instruction to asm.'''
        pass
        
class Subroutine():
    def __init__(self, name, body):
        self.name = name
        self.body = body
        
    def format(self):
        '''Return asm formatted code.'''
        pass