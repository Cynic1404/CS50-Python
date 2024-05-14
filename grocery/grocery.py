checker={}
order=[]
while True:
    try:
        item = input()
    except EOFError:
        for product in sorted(order):
            print(f"{checker[product]} {product}")
        break
    else:
        item=item.upper()
        if item not in order:
            order.append(item)
        if item in checker:
            checker[item]=checker[item]+1
        else:
            checker[item]=1

