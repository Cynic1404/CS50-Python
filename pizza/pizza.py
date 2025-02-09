import sys
import csv
import tabulate

def main():

    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")

    else:
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            try:
                new_list=[]
                with open(sys.argv[1]) as file:
                    reader = list(csv.reader(file))

                    return tabulate.tabulate(reader[1:], headers=reader[0], tablefmt="grid")
            except FileNotFoundError:
                sys.exit("File does not exist")


if __name__=="__main__":
    print(main())
