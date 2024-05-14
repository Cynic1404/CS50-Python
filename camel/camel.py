def main():
    message=input("CamelCase: ")
    for i in message:
        if i.isupper():
            message=message.replace(i, f"_{i.lower()}")
    print(f"snake_case: {message}")


if __name__ == "__main__":
    main()
