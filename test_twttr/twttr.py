def main():
    message = input("Input: ")
    print(shorten(message))


def shorten(word):
    for i in word:
        if i in 'aAoOuUiIeE':
            word=word.replace(i, '')
    return word

if __name__ == "__main__":
    main()
