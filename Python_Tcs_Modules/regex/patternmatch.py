
import re
string = "contact me at imciiit@gmail.com"
match = re.search("([\w]+)(@)([\w]+)(.)([\w]{2,3})", string)
if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    print(match.group(4))
    print(match.group(5))
    
else :
    print("No Match")
