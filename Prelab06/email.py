#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-10-04 18:02:27 -0400 (Sun, 04 Oct 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Prelab06/email.py $
#$Revision: 82407 $
import re
import sys
import os

def get_email(file):
    if not os.access(file,os.R_OK):
        print('Error: Could not read {}'.format(file))
        exit()

    with open(file, 'r') as f:
        data = f.readlines()

    expr = re.compile(r'@purdue.edu')
    expr2 = re.compile('\d*\.\d+')
    for item in data:
        out = re.sub(expr,'@ecn.purdue.edu',item)
        email = out.split()[0]
        num = out.split()[1]
        num = re.sub(expr2,'{}/100'.format(num),num)
        print('{0:30}{1:10}'.format(email,num))

if __name__ == "__main__":

    if(len(sys.argv) != 2):
        print('Usage: email.py [filename.in]')
        exit()

    file = sys.argv[1]
    get_email(file)