import random


def main():
    l = get_level()
    count=0
    for _ in range(10):
        a = generate_integer(l)
        b = generate_integer(l)
        for _ in range(3):
            solution = input(f"{a} + {b} = ")
            if solution.isdigit():
                if int(solution) == a + b:
                    count += 1
                    break
                else:
                    print("EEE")
            else:
                print("EEE")
        print(f"{a} + {b} = {a+b}")
    print(f"Score: {count}")



def get_level():
    while True:
        level = input("Level: ")
        if level not in ["1", "2", "3"]:
            continue
        else:
            return int(level)


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)


if __name__ == "__main__":
    main()
