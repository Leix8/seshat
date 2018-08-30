#!/usr/bin/env python

#pre: this script needs seshat binary file compiled completely and put into the same directory
#usage: (in command line) python3 py-seshat.py <input file> <output directory>
#for example: python3 py-seshat.py ./SampleMathExps/exp.scgink output
#output files will be put into output folder defined in command line and named out.*



import os 
import sys

def interface(input_file,output_dir):
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    file_inkml=output_dir+"/out.inkml"
    file_pgm =output_dir+"/out.pgm"
    file_dot=output_dir+"/out.dot"

    p=os.popen("./seshat -c Config/CONFIG -i"+input_file+ " -o "+ file_inkml +" -r "+ file_pgm + " -d "+file_dot)
    while 1:
        line=p.readline()
        if  ''==line:
            break
        print (line)

if __name__=='__main__':

    input_file,output_dir=sys.argv[1],sys.argv[2]
    
    interface(input_file,output_dir)
