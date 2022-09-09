import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Valid input & output
    # 9:00 AM to 5:00 PM ->  09:00 to 17:00
    # 9 AM to 5 PM       ->  09:00 to 17:00
    if matches := re.search(r'((1[0-2]|[1-9]):([0-5][0-9]) (AM|PM) to (1[0-2]|[1-9]):([0-5][0-9]) (AM|PM))|((1[0-2]|[1-9]) (AM|PM) to (1[0-2]|[1-9]) (AM|PM))', s):
        List = list(matches.groups())
        if (List[0] != None):
            if matches.group(4) == 'PM':
                From = str((12 + (int(matches.group(2))%12))%24)
            else:
                From = str((12 + int(matches.group(2))) % 12)
            if matches.group(7) == 'PM':
                To = str((12 + (int(matches.group(5))%12))%24)
            else:
                To = str((12 + int(matches.group(5))) % 12)
            return From.zfill(2) + ":" + matches.group(3) + " to " +  To.zfill(2) + ":" + matches.group(6)

        else: # start with index 8
            if matches.group(10) == 'PM':
                From =  str((12 + (int(matches.group(9))%12))%24)
            else:
                From = str((12 + int(matches.group(9))) % 12) 
            if matches.group(12) == 'PM':
                To = str((12 + (int(matches.group(11))%12))%24) 
            else:
                To = str((12 + int(matches.group(11))) % 12) 
            return From.zfill(2) + ":00" + " to " +  To.zfill(2) + ":00"
    else:
         raise ValueError
if __name__ == "__main__":
    main()