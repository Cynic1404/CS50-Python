import re


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    if matches := re.search(r"^([1][0-2]?|[1-9])(?::([0-5][0-9]))? (AM|PM) to ([1][0-2]?|[1-9])(?::([0-5][0-9]))? (AM|PM)$", s):
        from_hours, from_minutes, from_datetime,  to_hours, to_minutes, to_datetime = matches.groups()

        if from_hours==to_hours=="12" and (to_minutes==from_minutes=="00" or to_minutes==from_minutes==None):
            return "00:00 to 12:00"

        if to_datetime == "PM":
            if to_hours == "12":
                to_hours = "00"
            else:
                to_hours = str(int(to_hours)+12)

        if from_datetime == "PM":
            if from_hours == "12":
                from_hours = "00"
            else:
                from_hours = str(int(from_hours)+12)

        if not from_minutes:
            from_minutes = "00"

        if not to_minutes:
            to_minutes = "00"
        return f"{int(from_hours):02}:{from_minutes} to {int(to_hours):02}:{to_minutes}"
    raise ValueError("wrong format")






if __name__ == "__main__":
    main()
