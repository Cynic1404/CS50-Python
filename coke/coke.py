def main():
    money_needed = 50
    while money_needed > 0:
        coin = input("Insert Coin: ")
        if coin in ["5","10","25"]:
            money_needed-=int(coin)
            if money_needed>0:
                print(f"Amount Due: {money_needed}")
            else:
                print(f"Change Owed: {-money_needed}")
        else:
            print(f"Amount Due: {money_needed}")



if __name__ == "__main__":
    main()
