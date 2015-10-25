#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2015-08-30 18:09:13 -0400 (Sun, 30 Aug 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Prelab01/svncheck.bash $
#$Revision: 80456 $


if [[ $# != 1 ]]
then
    echo "Please give one and only one file list!"
    exit 1

else
    for line in $(cat $1)
    do
        file=$line
        STATUS=$(svn status $file | head -c 1)
        
        if [[ -e $file && (( $STATUS == '?' )) ]]
        then         
            if [[ ! -x $file ]]
            then
                echo -n "Would you like to make $file executable?(y/n): " 
                read check
                if (( check == 'y' ))
                then
                    chmod +x $file
                    svn add $file
                fi
            else
                svn add $file
            fi

        elif [[ (( ! -x $file )) && (( $STATUS == ' ' )) ]]
        then
            svn propset svn:executable ON $file
        fi

        if [[ ! -e $file ]]
        then
            echo "Error: File $file appears to not exist here or in svn"
        fi

    done

fi
echo "Auto-committing code"
svn commit -m "Code auto-committed through svncheck.bash"
exit 0
        


