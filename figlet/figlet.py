import sys
import pyfiglet
figlet = pyfiglet.Figlet()

if len(sys.argv)==3 and sys.argv[1] in (["-f", "--font"]) and sys.argv[2] in figlet.getFonts():
    message = input("Input: ")
    f = pyfiglet.figlet_format(message, font=sys.argv[2])
    print(f)
else:
    sys.exit("wrong format")


