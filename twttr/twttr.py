def main():
    message = input("Input: ")
    for i in message:
        if i in 'aAoOuUiIeE':
            message=message.replace(i, '')
    print(message, end="")

if __name__ == "__main__":
    main()
