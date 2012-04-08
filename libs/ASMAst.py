

class ASMObject(object):
    name = "ASTObject"
    instruction = "ASMObject"

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def toASM(self):
        return "{0} {1}, {2}".format(self.instruction, self.arg1, self.arg2)

    def __str__(self):
        return str(self.toASM())

    def __repr__(self):
        return repr(str(self))


class ASMSet(ASMObject):
    """0x1: SET a, b - sets a to b"""
    instruction = "SET"


class ASMAdd(ASMObject):
    """0x2: ADD a, b - sets a to a+b, sets O to 0x0001 if there's an overflow,
    0x0 otherwise"""
    instruction = "ADD"


class ASMSub(ASMObject):
    """0x3: SUB a, b - sets a to a-b, sets O to 0xffff if there's an underflow,
    0x0 otherwise"""
    instruction = "SUB"


class ASMMul(ASMObject):
    """0x4: MUL a, b - sets a to a*b, sets O to ((a*b)>>16)&0xffff"""
    instruction = "MUL"


class ASMDiv(ASMObject):
    """0x5: DIV a, b - sets a to a/b, sets O to ((a<<16)/b)&0xffff. if b==0,
    sets a and O to 0 instead"""
    instruction = "DIV"


class ASMMod(ASMObject):
    """0x6: MOD a, b - sets a to a%b. if b==0, sets a to 0 instead."""
    instruction = "MOD"


class ASMShl(ASMObject):
    """0x7: SHL a, b - sets a to a<<b, sets O to ((a<<b)>>16)&0xffff"""
    instruction = "SHL"


class ASMShr(ASMObject):
    """0x8: SHR a, b - sets a to a>>b, sets O to ((a<<16)>>b)&0xffff"""
    instruction = "SHR"


class ASMAnd(ASMObject):
    """0x9: AND a, b - sets a to a&b"""
    instruction = "AND"


class ASMBor(ASMObject):
    """0xa: BOR a, b - sets a to a|b"""
    instruction = "BOR"


class ASMXor(ASMObject):
    """0xb: XOR a, b - sets a to a^b"""
    instruction = "XOR"


class ASMIfe(ASMObject):
    """0xc: IFE a, b - performs next instruction only if a==b"""
    instruction = "IFE"


class ASMIfn(ASMObject):
    """0xd: IFN a, b - performs next instruction only if a!=b"""
    instruction = "IFN"


class ASMIfg(ASMObject):
    """0xe: IFG a, b - performs next instruction only if a>b"""
    instruction = "IFG"


class ASMIfb(ASMObject):
    """0xf: IFB a, b - performs next instruction only if (a&b)!=0"""
    instruction = "IFB"


class ASMFunction(ASMObject):
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def toASM(self):
        asm = ":"
        asm += self.name
        asm += "\n"

        for child in self.children:
            asm += "\t{0}\n".format(child.toASM())

        return asm

if __name__ == "__main__":

    Set = ASMSet("a", "0x10")
    func = ASMFunction("test")
    func.addChild(Set)
    func.addChild(Set)
    func.addChild(Set)
    func.addChild(Set)

    print func
