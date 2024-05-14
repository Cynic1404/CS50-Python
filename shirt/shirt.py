import sys
from PIL import Image, ImageOps


def main():


    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")

    else:
        if not sys.argv[1].endswith(".jpg") and not sys.argv[1].endswith(".png") and not sys.argv[1].endswith(".jpeg"):
            sys.exit("Invalid output")
        elif sys.argv[1].split(".")[-1] != sys.argv[2].split(".")[-1]:
                sys.exit("Input and output have different extensions")
        else:
            try:
                shirt = Image.open("shirt.png")
                size = shirt.size
                photo = Image.open(sys.argv[1])
                photo = ImageOps.fit(photo, size)
                photo.paste(shirt, shirt)
                photo.save(sys.argv[2])
            except FileNotFoundError:
                sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
