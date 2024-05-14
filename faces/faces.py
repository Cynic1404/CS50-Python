def convert(text_to_convert):
    text_to_convert=text_to_convert.replace(":)","🙂")
    text_to_convert=text_to_convert.replace(":(","🙁")
    print(text_to_convert)

if __name__ == "__main__":
    message = input()
    convert(message)

