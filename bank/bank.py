message = input("Greeting: ").lower().strip()

if message.startswith("hello"):
        print("$0")
elif message.startswith("h"):
        print("$20")
else:
        print("$100")
