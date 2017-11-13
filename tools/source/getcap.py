#!/usr/bin/env python3

# by SuperR. @XDA

import sys, os, struct

lenarg = len(sys.argv)
if lenarg < 2:
    print()
    print('Usage: getcap.py path/to/file [ h ]')
    print()
    print('h - hex format (decimal is default)')
    print()
    print('Example:')
    print('./getcap.py system/bin/run-as h')
    sys.exit()
else:
    p = sys.argv[1]
    f = None
    if lenarg > 2:
        f = str(sys.argv[2])
    
    try:
        b = os.getxattr(p, "security.capability")
        cap = str(list(struct.unpack("<IIIII", b))[1])
        if f == 'h':
            print(p, hex(int(cap)))
        else:
            print(p, cap)

    except:
        pass