#!/usr/bin/env python3

# by SuperR. @XDA

import sys, os, struct, argparse

parser = argparse.ArgumentParser(description="Retrieve file capabilities from a file.")
group = parser.add_mutually_exclusive_group()
group.add_argument("-x", "--hex", action="store_true", help="Returns file capability in hex format (default is decimal)")
parser.add_argument("filename", help="Path to the working file")
args = parser.parse_args()

try:
    b = os.getxattr(args.filename, "security.capability")
    cap = str(list(struct.unpack("<IIIII", b))[1])
    if args.hex:
        print(args.filename, hex(int(cap)))
    else:
        print(args.filename, cap)
except:
    pass
