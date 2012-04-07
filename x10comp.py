#! /usr/bin/env python
# Code Copyright (c) 2012 <aj00200@aj00200.org>
# Want it under a free license? Just ask!!!

import sys
import parsers.cparse
import converters.c2x10c

def main():
    if len(sys.argv) == 1:
        print(' Usage: x10comp.py [file.c]')
        exit()
        
    filename = sys.argv[-1]
        
    parser = parser.cparse.Parser(filename)
    converter = converters.c2x10c.Converter()
    
if __name__ == '__main__':
    main()