def main():
   message=input("What time is it? ")
   if 7<=convert(message)<=8:
       print("breakfast time")
   elif 12 <= convert(message) <=13:
       print("lunch time")
   elif 18 <= convert(message) <=19:
       print("dinner time")





def convert(time):
    hours, minutes=time.split(":")
    return float(hours)+float(minutes)/60


if __name__ == "__main__":
    main()
