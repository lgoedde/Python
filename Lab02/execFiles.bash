#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2015-09-08 17:20:01 -0400 (Tue, 08 Sep 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Lab02/execFiles.bash $
#$Revision: 81701 $

files=$(ls c-files)
files=($files)

for file in ${files[*]}
do
    echo -n "Compiling file $file..."
    gcc -Wall -Werror c-files/$file 2>/dev/null
    check=$?
    if [[ $check == '0' ]]
    then
        echo "Compilation succeeded."
        file=$(echo $file | cut -d'.' -f1)
        ./a.out > $file.out
    else
        echo "Error: Compilation failed."
    fi

done

exit 0
