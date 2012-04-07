#! /usr/bin/env python
# Copyright 2012 Aj00200 <aj00200@aj00200.org>
# Licensed under the GNU GPL v3

import sys
import parsers.cparse
import converters.c2x10c

def main():
    if len(sys.argv) == 1:
        print(' Usage: x10comp.py [file.c]')
        exit()
        
    filename = sys.argv[-1]
        
    parser = parsers.cparse.Parser(filename)
    converter = converters.c2x10c.Converter(parser)
    converter.convert()
    
if __name__ == '__main__':
    main()