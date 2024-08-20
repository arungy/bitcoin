#!/usr/bin/env python

import sys
import os
import array
import struct 

def usage():
    print('usage: python ppmio.py in_file.ppm')
    sys.exit(1)

def partition(s, ch):
    if (ch in s):
        i = s.index(ch)
        return (s[0:i], s[i], s[i+1:])
    else:
        return (s, None, None)

def strip_comment(s):
    (rval, junk1, junk2) = partition(s, '#')
    return rval.rstrip(' \t\n')

def read_ppm_header(filename):
    print('file name : %s' % (filename))
    linefeed = "\n"
    
    outdata = ''
    with open(filename, 'r+') as fr:
        try:
            line1 = fr.readline().strip().rstrip()
            line2 = fr.readline().strip().rstrip()
            line3 = fr.readline().strip().rstrip()
            data = fr.readlines()
            
            dim = line2.split(' ')
            w = int(dim[0])
            h = int(dim[1])
            mv = int(line3)
        except:
            print('Error: %s file open error' % (filename))
            sys.exit(1)
    fr.close()

    indata = bytes(data)
    print(int(struct.unpack('b', indata[0:1]))) 
    #for y in range(0, h):
    #    for x in range(0, w):
    #        idx = y * w + x
    #        r = indata[(w * h * 0) + idx]
    #        g = indata[(w * h * 1) + idx]
    #        b = indata[(w * h * 2) + idx]
    #        
    #        print(indata)
    #        break
    #    break
    #        
    #        #y = (0.299    * float(r)) + (0.587    * float(g)) + (0.114    * float(b))
    #        #u = (-0.14713 * float(r)) + (-0.28886 * float(g)) + (0.436    * float(b))
    #        #v = (0.615    * float(r)) + (-0.51499 * float(g)) + (-0.10001 * float(b))
    #        #
    #        #outdata.append(int(y))
    #        #outdata.append(int(u))
    #        #outdata.append(int(v))
    #        #image[x].append(int(data[(y * w + x) * 3]), int(inData[(y * w + x) * 3 + 1]), int(inData[(y * w + x) * 3 + 2]))
    
    if line1.upper() == 'P6':
        outFileName = 'tmp.ppm'
        with open(outFileName, 'wb') as fw:
            try:
                print('width: %d, height: %d' % (w, h))
                print('maxval: %d' % (maxval))
                header = str('P6') + linefeed + str(w) + str(' ') + str(h) + linefeed + str(maxval) + linefeed
                fw.writelines(header)
                fw.writelines(outdata)
            except:
                print('Error: %s file open error' % (outFileName))
                sys.exit(1)
        fw.close()

def read_ppm_data(f, w, h):
    #inData = array.array('B', [0, 0, 0] * w * h)

    #print (w * h)
    inData = []
    for line in f:
        line = strip_comment(line)
        inData += line.split(' ')
        
    #print int(inData[0])
    
    image = []
    for x in range(0, w):
        image.append([])
        for y in range(0, h):
            image[x].append(int(inData[(y * w + x) * 3]), int(inData[(y * w + x) * 3 + 1]), int(inData[(y * w + x) * 3 + 2]))
            
    #print image[0][0]
          
    return None
    
def call_ppmio(filename):
    read_ppm_header(filename)

if __name__ == '__main__':
    if len(sys.argv) != 2: 
        usage()
    
    call_ppmio(sys.argv[1])
    sys.exit(0)
    
