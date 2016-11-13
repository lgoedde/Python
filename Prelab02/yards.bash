#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2015-09-04 14:33:51 -0400 (Fri, 04 Sep 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Prelab02/yards.bash $
#$Revision: 81361 $

if [[ $# != 1 ]]
then
    echo "Usage: ./yards.bash <filename>"
    exit 1
fi

if [[ ! -r $1 ]]
then
    echo "Error: $1 is not readable"
    exit 2
fi

max=0

while read line 
do
    conf=$(echo $line | cut -d' ' -f1)
    yards=$(echo $line | cut -d' ' -f2-)
    yards=($yards)
    total=${#yards[*]}
    sum=0
    difftot=0

    for item in ${yards[*]}
    do
        ((sum=$sum+$item))
    done

    ((avg=$sum/$total))
    
    if [[ $avg > $max ]]
    then 
        max=$avg
    fi


    for item in ${yards[*]}
    do
        ((diff=$item - $avg))
        ((diff=$diff ** 2))
        ((difftot=$difftot + $diff))
    done

    ((var=$difftot/$total))
    
    echo "$conf schools averaged $avg yards receiving with a variance of $var"

done < $1

echo "The largest average yardage was $max"

exit 0

