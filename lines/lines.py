import sys
import requests


if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")

else:
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        try:
            count=0
            with open (sys.argv[1]) as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    if line and not line.startswith("#"):
                            count+=1
        except FileNotFoundError:
            sys.exit("File does not exist")
print(count)
