import datetime
import inflect
import sys

p = inflect.engine()


def main():
    dob = input("Date of Birth: ")
    print(convert(dob))


def convert(time, start_from=None):
    try:
        datetime_object = datetime.datetime.strptime(time, '%Y-%m-%d').date()
    except ValueError:
        sys.exit("Invalid date")

    #start_from added to add flexibility for test cases. The same tests will be working every day with no hardcoded data
    #try/except part can be moved to the main function, but test will need to be changed
    if start_from:
        minutes = int(
            (datetime_object - datetime.datetime.strptime(start_from, '%Y-%m-%d').date()).total_seconds() // 60)
    else:
        minutes = int((datetime.date.today() - datetime_object).total_seconds() // 60)
    return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"


if __name__ == "__main__":
    main()
