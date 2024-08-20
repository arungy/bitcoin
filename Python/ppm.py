#!/usr/bin/python -tt

"""
ppm.py -- just a little example python program
to read and write PPM file. This program works.

-tt flag above detects space/tab indent problems
"""

#sys is one of many available modules of library code, import to use.
#sys.argv is the list of command line arguments.
import sys

#defines a global variable
a = 123 

# define a 'read_ppm' function which takes a filename
def read_ppm(filename):
    """Given filename, print its text contents."""
    print(filename, '=======')
    fmt = "utf-8"

    ppm_hdr = []
    ppm_dat = []

    f = open(filename, 'rb')
    
    while True:
        ln = f.readline()
        ln = ln.decode(fmt)
        ln = ln.strip()

        if '#' in ln:
            continue
        
        ln = ln.split()        
        ppm_hdr.append(ln)
        
        if 1 == len(ln) and ln[0].isnumeric():  # after maxvalue is read, break the header reading
            break;

    ppm_dat = f.read()
    f.close()
    
    filetype = "".join(ppm_hdr[0])
    width    = int(ppm_hdr[1][0])
    height   = int(ppm_hdr[1][1])
    maxval   = int(ppm_hdr[2][0])
    
    print(filetype, width, height, maxval)

def main():
    # sys.argv contains command line arguments.
    # This assigns a list of all but the first arg into a local 'args' var.
    args = sys.argv[1:]
    
    if len(args) == 1:
        read_ppm(args[0])
        print('all done') # this print is outside the loop, due to its indentation
    else:
        print('usage: ppm.py test.ppm')

# Standard boilerplate at end of file to call main() function.
if __name__ == '__main__':
    main()
