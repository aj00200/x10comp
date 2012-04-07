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
        
    def cinstr_dig(self):
        '''Recursively search through the AST until the bottom is
        reaced. Work backwards, calling cfunc2asm at each level from
        the bottom to top.
        '''
        block_stack = []
        
    def cfunc2asm(self, function):
        '''Take a pycparser function as input and output the 0x10c asm.'''
        print(' [*] Inside function:')
        funcbody = function.children()[1][1]
        funcbody_instructions = funcbody.children()
        funcbody.show()
        
        for instruction in funcbody_instructions:
            instr = instruction[1]
            instr.show()
            print(self.cinstr2asm(instr))
                
    def cinstr2asm(self, instruction):
        '''Convert a single instruction to asm.'''
        if isinstance(instruction, pycparser.c_ast.Assignment):
            pass # SET a,b
        elif isinstance(instruction, pycparser.c_ast.BinaryOp):
            pass # AND, BOR, XOR, IFE, IFN, IFG, IFB
            
        elif isinstance(instruction, pycparser.c_ast.Constant):
            return instruction.value
        
class Subroutine():
    def __init__(self, name, body):
        self.name = name
        self.body = body
        
    def format(self):
        '''Return asm formatted code.'''
        pass