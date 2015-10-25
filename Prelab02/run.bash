#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2015-09-06 21:33:02 -0400 (Sun, 06 Sep 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Prelab02/run.bash $
#$Revision: 81456 $

if [[ $# != 2 ]]
then 
    echo "Usage: ./run.bash <source filename> <output filename>"
    exit 1
fi

if [[ -e $2 ]]
then
    echo -n "$2 exists. Would you like to delete it?" 
    read check
    
    if [[ $check == 'yes'  || $check == 'y' ]]
    then 
        rm -f $2
        touch $2
        outfile=$2
    else
        read -p "Enter a new filename: " outfile
    fi
else
    touch $2
    outfile=$2
fi

gcc $1 -o quick_sim 
if [[ $? != 0 ]]
then
    echo "error: quick_sim could not be compiled!"
    exit 2 
else
    cache=(1 2 4 8 16 32)
    width=(1 2 4 8 16)
    for cnum in ${cache[*]}
    do 
        for wnum in ${width[*]}
        do
            output=$(quick_sim $cnum $wnum a)
            proc=$(echo $output | cut -d':' -f2)
            csize=$(echo $output | cut -d':' -f4)
            iwidth=$(echo $output | cut -d':' -f6)
            cpi=$(echo $output | cut -d':' -f8)
            etime=$(echo $output | cut -d':' -f10)
            echo "$proc:$csize:$iwidth:$cpi:$etime" >> $outfile

            output=$(quick_sim $cnum $wnum i)
            proc=$(echo $output | cut -d':' -f2)
            csize=$(echo $output | cut -d':' -f4)
            iwidth=$(echo $output | cut -d':' -f6)
            cpi=$(echo $output | cut -d':' -f8)
            etime=$(echo $output | cut -d':' -f10)
            echo "$proc:$csize:$iwidth:$cpi:$etime" >> $outfile

        done
    done
    min=1000000
    while read line
    do
        curr=$(echo $line | cut -d':' -f5)
        if [[ $curr -le $min ]]
        then
            min=$curr
            proc1=$(echo $line | cut -d':' -f1)
            csize1=$(echo $line | cut -d':' -f2)
            iwidth1=$(echo $line | cut -d':' -f3)

        fi
    done < $outfile
    echo "Fastest run time achieved by $proc1 with cache size $csize1 and issue width $iwidth1 was $min"
fi

exit 0 
