'''
เข้าใจขื้น ถ้าใส่ตัวแปล
x = (" "*(Number-floor)
y = ("*"*(floor*2+1)
'''
Number = int(input("Plase enter your Number :"))
for floor in range(Number):
    print((" "*(Number-floor))+("*"*(floor*2+1)))
