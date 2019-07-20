def Login():
    Username = input("Plase enter your Username :")
    Password = input("Plase enter your Password :")
    while Username != "asd" or Password != "123":
        print("Usename or Password is incorrect")
        print("Plase try again!!")
        Username = input("Plase enter your Username :")
        Password = input("Plase enter your Password :")
    ShowMenu()
def ShowMenu():
    print("---------Calculate Program--------")
    print("if you want to use Vat Calculate press ->1")
    print("if you want to use Price Calculate press ->2")
    print("if you want to Total your Price and Vat together press ->3")
    MenuSelect()

def MenuSelect():
    Choice = int(input("Plase Choose the Choice :"))
    if Choice == 1:
        print("----------------------------")
        print("Vat = ",VatCalculate(),"THB")
    elif Choice == 2:
        print("-----------------------------------")
        print("TotalPrice :",PriceCalculate(),"THB")
    elif Choice == 3:
        print("---------------------------------------")
        print("Grand_Price = ",PriceCalculate_1(),"THB")


def VatCalculate():
    print("--------------------------------")
    print("1.You want to use Vat Calculate.")
    TotalPrice = 0
    Item = int(input("How many Item do you have :"))
    for Number in range(Item):
        Price = int(input(str(Number + 1) + ". Plase enter your Price :"))
        TotalPrice += Price
    Vat = 7
    VatPrice = TotalPrice*Vat/100
    return VatPrice


def PriceCalculate():
    print("---------------------------------")
    print("2.You want to use Price Calculate.")
    TotalPrice = 0
    Item = int(input("How many Item do you have :"))
    for Number in range(Item):
        Price = int(input(str(Number+1)+". Plase enter your Price :"))
        TotalPrice += Price
    return TotalPrice


def VatCalculate_1(Price):
    Vat = 7
    VatPrice = Price + (Price * Vat / 100)
    return VatPrice
def PriceCalculate_1():
    print("-----------------------------------------------")
    print("3.You want to Total your Price and Vat together.")
    TotalPrice = 0
    Item = int(input("How many Item do you have :"))
    for Number in range(Item):
        Price = int(input(str(Number + 1) + ". Plase enter your Price :"))
        TotalPrice += Price
    return VatCalculate_1(TotalPrice)

Login()