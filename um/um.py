import re


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall(r"((?:U|(\su|^u))m)[.!?'\s,]*", s))



if __name__ == "__main__":
    main()
