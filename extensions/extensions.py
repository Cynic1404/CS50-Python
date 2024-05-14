message=input("File name: ").lower().strip()

format={
    "image":["gif", "jpg", "jpeg", "png"],
    "application":["pdf", "zip"],
}

extension = message.split(".")[-1].replace("\n", "")

for i in format:
    if extension in format[i]:
        if extension =="jpg":
            extension="jpeg"
        print(f"{i}/{extension}")
        break
    if extension=="txt":
        print("text/plain")
        break
else:
    print("application/octet-stream")

