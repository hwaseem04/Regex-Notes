import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'"(https?://)(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)"',s):
        if ("s" not in matches.group(1)):
            new_s =  "https://" + "youtu.be/" +  matches.group(2)
        else:
            new_s =  matches.group(1) + "youtu.be/" +  matches.group(2)
        return new_s
    else:
        return None


if __name__ == "__main__":
    main()