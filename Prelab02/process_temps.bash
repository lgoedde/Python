#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2015-09-07 16:59:58 -0400 (Mon, 07 Sep 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Prelab02/process_temps.bash $
#$Revision: 81517 $

if [[ $# != 1 ]]
then
    echo "Usage: process_temps.bash <input_file>"
    exit 1
fi

if [[ ! -r $1 ]]
then
    echo "Error: $1 is not a readable file."
    exit 2
fi

cat $1 | tail -n +2 > $1_noheader

while read line
do
    t=$(echo $line | cut -d' ' -f1)
    data=$(echo $line | cut -d' ' -f2-)
    data=($data)
    total=${#data[*]}
    sum=0
    
    for item in ${data[*]}
    do
        ((sum=$sum+$item))
    done
    
    ((avg=$sum/$total))
    
    echo "Average temperature for time $t was $avg C."

done < $1_noheader

rm -f *_noheader

exit 0
