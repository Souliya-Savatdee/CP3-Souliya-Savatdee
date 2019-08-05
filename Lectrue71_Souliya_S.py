MenuList = []
PriceList = []
Head = "Your Menu"

def ShowBill():
    AllPrice = 0
    rank = 0
    print(Head.center(30,"-"))
    for Num in range(len(MenuList)):
        rank += 1
        print("%s."%(rank),MenuList[Num]," Price :",PriceList[Num],"THB")
        AllPrice += int(PriceList[Num])
    print("ToTal Price : ",AllPrice,"THB")

while True:
    Menu_Name = input("Plase enter Manu :")
    while Menu_Name.isdecimal() == True:
        print("Don't have this Menu! Plase try again")
        Menu_Name = input("Plase enter Manu again:")
    if Menu_Name.capitalize() == "Exit":
        ShowBill()
        break
    else:
        Price_Number = input("Price :")
        while Price_Number.isdecimal() == False:
            print("This isn't the Price!! Plase try again")
            Price_Number = input("Price again :")
        MenuList.append(Menu_Name)
        PriceList.append(Price_Number)

