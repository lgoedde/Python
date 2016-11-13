#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-10-27 17:49:08 -0400 (Tue, 27 Oct 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Lab08/verilog2vhdl.py $
#$Revision: 83047 $
from vtools import *
def convertLine(verilogLine):
    try:
        (comp,inst,netlist) = parseNetLine(verilogLine)
        mystr = ''
        mystr += '{}: {} PORT MAP('.format(inst,comp)

        for i, item in enumerate(netlist):
            if i == len(netlist) - 1:
                mystr+= '{}=>{});'.format(item[0],item[1])
            else:
                mystr+= '{}=>{}, '.format(item[0],item[1])

        print(mystr)
        return mystr
    except:
        return("Error: Bad Line.")

def convertFile(sourceFile,targetFile):
    with open(sourceFile, 'r') as f:
        data = f.readlines()

    mystr = ''
    for item in data:
        mystr += convertLine(item) + '\n'

    with open(targetFile, 'w') as f2:
        f2.write(mystr[0:-1])



if __name__ == "__main__":
    convertLine("  OAI22X1     U11  (.A(n32),.B(n5),.C(n3),.D(n6),.Y(n25))")
