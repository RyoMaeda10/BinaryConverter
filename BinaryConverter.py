from tokenize import String

def convert(num):
    Base10 = int(num)
    print(Base10, "in binary is", bin(Base10).replace("0b",""))

def change(number):
    Base2 = int(number)
    Ans = int(number, 2)
    print(Base2, "In Base10 is", Ans) 



x = input("What kind of number would you like to convert? (Base10 or Base2) ")

if x == "Base10":
    y = input("Enter your number: ")
    convert(y)

elif x == "Base2":
    z = input("Enter your number: ")
    change(z)
