# Check for python version

from platform import python_implementation, python_version_tuple

print(python_implementation())

for i in python_version_tuple():
    print(i)
