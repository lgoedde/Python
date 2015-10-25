__author__ = 'ee364e07'

import re

expr = re.compile("^((00[0-9]|0[1-9][0-9]|[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}(00[0-9]|0[1-9][0-9]|[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
string = '010.10.10.255'

test = re.match(expr,string)

if test:
    print("Valid IP Address")

else:
    print("Error: Not a valid IP Address")

re.search("e", input, re.I)






