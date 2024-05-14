names=[]

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        if len(names)==2:
            print(f"Adieu, adieu, to {', '.join(names[:-1])+' and '+names[-1]}")
        elif len(names)>2:
            print(f"Adieu, adieu, to {', '.join(names[:-1])+', and '+names[-1]}")
        elif len(names)==1:
            print(f"Adieu, adieu, to {names[0]}")
        break
