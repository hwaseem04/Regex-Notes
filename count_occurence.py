import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if matches := re.findall(r"\b[u][m]\b", s, re.IGNORECASE):
        return len(matches)
    else:
        pass

if __name__ == "__main__":
    main()