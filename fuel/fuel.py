
def main():
    while True:
        message = input("Fraction: ")
        percent = convert(message)
        if percent or percent==0:
            break

    print(gauge(percent))


def convert(fraction):
    try:
        x,y = fraction.split("/")
        x=int(x)
        y=int(y)
        if x>y:
            return None
        else:
            res = round(x / y * 100)
            return res

    except (ValueError):
        return None



def gauge(percentage):
    if 99<=percentage<=100:
        return "F"
    elif percentage<=1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()








