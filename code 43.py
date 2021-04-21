# Metacharacters(e-mail extraction)
import re

pattern = r"([\w\._]+)@([\w\._]+)(\.[\w\.]+)"
str = "Please contact roysuvam1999@gmail.com for more help"

match = re.search(pattern, str)
if match:
    print(match.group())
