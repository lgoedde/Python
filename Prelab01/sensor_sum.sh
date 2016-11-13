#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2015-08-30 18:10:32 -0400 (Sun, 30 Aug 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Prelab01/sensor_sum.sh $
#$Revision: 80458 $

if [[ $# != 1 ]]
then
    echo "usage: ./sensor_sum.sh <filename>"
    exit 1

elif [[ ! -r $1 ]] 
then 
    echo "error: $1 is not a readable file!"
    exit 1

else
    while read line
    do
        sensor=$(echo $line | cut -d'-' -f1) #get the sensor number
        echo -n $sensor
        echo -n " "
        var1=$(echo $line | cut -d' ' -f2) #get each of the values
        var2=$(echo $line | cut -d' ' -f3)
        var3=$(echo $line | cut -d' ' -f4)
        ((total= $var1 + $var2 + $var3)) #add them up
        echo $total #display the total
    done < $1

fi
exit 0
