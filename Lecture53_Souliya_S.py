def vatCalculate(TotalPrice):
    result = TotalPrice+(TotalPrice*7/100)
    return result
Price = int(input("Price (THB) :"))
print("Total Price :",vatCalculate(Price),"THB")