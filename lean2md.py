#!/usr/bin/python
import re
import sys
import getopt
import itertools

def process(inputfile, outputfile):
    with open(inputfile, 'r') as i, open(outputfile, 'w+') as o :
        is_md : bool = False
        should_ignore : bool = False
        output : list[str] = []
        # empty = True
        content = enumerate(i.readlines())
        for num_of_line, line in content:
            if line.startswith('--BEGIN:IGNORE'):
                should_ignore = True
            if line.startswith('--END:IGNORE'):
                should_ignore = False
                continue
            if line.startswith('/-MD'):
                is_md = True
                continue
            if line.startswith('MD-/'):
                is_md = False
                continue
            if should_ignore : continue
            if is_md:
                output.append(('MD', line))
            else:
                output.append(('LEAN', line))
        for k, items in itertools.groupby(output, lambda s: s[0]):
            if k == 'LEAN':
                code = ''.join(map(lambda s: s[1], items))
                if code.isspace(): continue
                else:
                    o.write('```lean\n')
                    o.write(code.strip())
                    o.write('\n```\n')
            if k == 'MD':
                for item in items: 
                    # print(item[1])
                    o.write(item[1])

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
       opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
       print ('test.py -i <inputfile> -o <outputfile>')
       sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('lean2md.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    process(inputfile, outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])