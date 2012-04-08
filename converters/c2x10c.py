import pycparser
import converters.base

class Converter(converters.base.Converter):
    '''Convert the code accessed through the parser object into asm.'''
    MAX_RAM = hex(0xffff)
    
    def __init__(self, parser):
        super(Converter, self).__init__(parser)
        self.subroutines = {}
        self.variables = {}
        self.next_free_ram = 0
    
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
        block_stack = [] # Contains Block objects
        
    def cfunc2asm(self, function):
        '''Take a pycparser function as input and output the 0x10c asm.
        Call cinstr_dig on each function to convert it to asm.
        TODO: pass loops and if statements back to this function.
        '''
        print(' [*] Inside function:')
        funcbody = function.children()[1][1]
        funcbody_instructions = funcbody.children()
        
        for instruction in funcbody_instructions:
            instr = instruction[1]
            # Check if we will need to handle the loop somehow
            if isinstance(instr, pycparser.c_ast.While):
                pass
            elif isinstance(instr, pycparser.c_ast.For):
                pass
                
            print(self.cinstr2asm(instr))
                
    def cinstr2asm(self, instruction):
        '''Convert a single instruction to asm. This method is called by
        cinstr_dig for every operation in the C code.
        '''
        #instruction.show()
        if isinstance(instruction, pycparser.c_ast.Assignment):
            a = self.cinstr2asm(instruction.children()[0][1])
            b = self.cinstr2asm(instruction.children()[1][1])
            return 'SET %s,%s' % (a, b)
        
        elif isinstance(instruction, pycparser.c_ast.BinaryOp):
            pass # AND, BOR, XOR, IFE, IFN, IFG, IFB
            
        elif isinstance(instruction, pycparser.c_ast.Constant):
            if instruction.type == 'int':
                return hex(int(instruction.value))
            elif instruction.type == 'float':
                raise UnsupportedCode('Float values are not supported yet.')
            
        elif isinstance(instruction, pycparser.c_ast.Decl):
            a = self.cinstr2asm(instruction.children()[0][1])
            b = self.cinstr2asm(instruction.children()[1][1])
            return 'SET %s,%s' % (a, b)

        elif isinstance(instruction, pycparser.c_ast.IdentifierType):
            if instruction.names == ['int']:
                return 1
            if instruction.names == ['char']:
                return 1
            elif instruction.names == ['float']:
                raise UnsupportedCode('Float values are not supported yet.')
            
            raise UnsupportedCode('Unknown memory size for data type: %s' %
                                  instruction.names)

        elif isinstance(instruction, pycparser.c_ast.TypeDecl):
            mem_size = self.cinstr2asm(instruction.children()[0][1])
            self.next_free_ram += mem_size
            return hex(self.next_free_ram - mem_size)
            
        elif isinstance(instruction, pycparser.c_ast.Constant):
            return instruction.value
        
class Subroutine(object):
    '''Hold asm code and output it with the subroutine name.'''
    def __init__(self, name, body):
        self.name = name
        self.body = body
        
    def format(self):
        '''Return asm formatted code.'''
        pass
        
class Block(object):
    def __init__(self, block):
        self.block = block
        self.index = 0
        self.total_blocks = len(block.children())
        
        
class UnsupportedCode(Exception):
    pass