#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-10-21 23:59:29 -0400 (Wed, 21 Oct 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Prelab08/listmod.py $
#$Revision: 82876 $

from math import floor

def find_median(List_1, List_2):
    
    merged = List_1 + List_2
    merged = sorted(merged)
    ind = floor((len(merged) - 1)/2)
    return (merged[ind],merged)

