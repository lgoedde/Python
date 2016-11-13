#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2015-08-25 22:42:40 -0400 (Tue, 25 Aug 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Prelab01/sum.bash $
#$Revision: 80214 $


sum=0
while (($# != 0))
do
    ((sum=sum+$1))
    shift

done

echo "$sum"

exit 0
