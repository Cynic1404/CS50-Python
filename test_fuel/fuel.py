
def main():
    while True:
        message = input("Fraction: ")
        percent = convert(message)
        if percent or percent==0:
            break

    print(gauge(percent))


def convert(fraction):
    x,y = fraction.split("/")
    x=int(x)
    y=int(y)
    if y == 0:
        raise ZeroDivisionError
    if x>y or x<0 or y<0:
        raise ValueError

    else:
        res = round(x / y * 100)
        return res




def gauge(percentage):
    if 99<=percentage<=100:
        return "F"
    elif percentage<=1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
