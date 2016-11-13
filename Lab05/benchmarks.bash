#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2015-09-29 16:40:36 -0400 (Tue, 29 Sep 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Lab05/benchmarks.bash $
#$Revision: 82275 $

if [[ $# != 1 ]]
then
    echo "Usage: ./benchmarks.bash <outputFile>"
    exit 1
fi

echo -n "Enter the array size(s): "
read arrs

echo -n "Enter the algorithm(s): "
read algs

echo -n "Enter column # to sort benchmarks: "
read col

while [[ $col < 2 || $col > 4 ]]
do
    echo "Error: invalid column number."
    echo -n "Enter column # to sort benchmarks: "
    read col
done

arrs=($arrs)
algs=($algs)

for item in ${arrs[*]}
do
    if [[ $item < 1 || $item == -1 ]]
    then
        echo "Error: invalid size of array"
        exit 2
    fi
done

for item in ${algs[*]}
do
    if [[ $item != 'shell' && $item != 'bubble' && $item != 'merge' && $item != 'sleep' ]]
    then
        echo "Error: invalid algorithm name."
        exit 5
    fi
done
newhead='size'

for item in ${arrs[*]}
do
    newhead=$newhead,$item
done
echo $newhead > $1

for alg in ${algs[*]}
do
    info=$alg

    for item in ${arrs[*]}
    do
        out=$(./sorting $item $alg)
        tim=$(echo $out | cut -d' ' -f3)
        info=$info,$tim
    done
    echo $info >> $1
done
cat $1 | tail -n +2 > $1.nohead
echo $newhead > $1.sorted 
cat $1.nohead | sort -n -k $col -t, >> $1.sorted

exit 0
