#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-10-04 18:03:10 -0400 (Sun, 04 Oct 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Prelab06/function_finder.py $
#$Revision: 82408 $

import re
import sys
import os

def get_functions(file):
    if not os.access(file,os.R_OK):
        print('Error: Could not read {}'.format(file))
        exit()

    expr = re.compile('def\ +(?P<func>[a-zA-Z][a-zA-Z0-9\-\_]*)\ *\((?P<args>[a-zA-Z0-9=\-\_,\ ]*)\):')

    with open(file, 'r') as f:
        data = f.readlines()

    for item in data:
        test = re.match(expr,item)

        if test:
            func = test.group('func')
            args = test.group('args').split(',')
            print(func)
            for i,item in enumerate(args,1):
                item = item.strip()
                print('Arg{}: {}'.format(i,item))


if __name__ == "__main__":

    if(len(sys.argv) != 2):
        print('Usage: function_finder.py [python_file_name]')
        exit()

    get_functions(sys.argv[1])

