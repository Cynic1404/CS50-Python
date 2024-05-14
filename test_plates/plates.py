def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 1<len(s)<7 and s.isalnum():
        if s[0].isalpha() and s[1].isalpha():
            if len(s)==2:
                return True
            else:
                for i in range(2, len(s)):
                    if s[i].isdigit():
                        if int(s[i])!=0:
                            if s[i:].isdigit():
                                return True
                            else:
                                return False
                        else:
                            return False
                    return True
    return False



if __name__ == "__main__":
    main()

