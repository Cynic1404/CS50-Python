import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r".*(?:\"|\')(?:http(?:|s)://)?(?:www.)?youtube.com/embed/(\w*)(\"|\')", s):
        return f"https://youtu.be/{matches.group(1)}"




if __name__ == "__main__":
    main()
