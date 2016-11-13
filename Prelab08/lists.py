#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-10-21 23:59:29 -0400 (Wed, 21 Oct 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Prelab08/lists.py $
#$Revision: 82876 $

from listmod import find_median

if __name__ == "__main__":
    flist = input("Enter the first list of numbers: ")
    slist = input("Enter the second list of numbers: ")
    flist = flist.split(' ')
    slist = slist.split(' ')

    flist = [int(x) for x in flist]
    slist = [int(x) for x in slist]
    (Median, Sorted_List) = find_median(flist,slist)
    print("First list: {}".format(flist))
    print("Second list: {}".format(slist))
    print("Merged list: {}".format(Sorted_List))
    print("Median: {}".format(Median))


