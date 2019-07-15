Username = input("Plase Login your Username :")
Password = input("Plase Login Your Password :")
if Username == "asd" and Password == "123":
    print("***********Welcome to Game Shop***************")
    print("**********************************************")
    print(">>if your want buy game press >>1")
    print(">>if your want buy Computer Hardware press >>2")
    print(">>if your want buy Computer Sofeware press >>3")
    Choice = int(input("Press Here : "))
    if Choice == 1:
        PUBG = 590
        DBDL = 690
        CSGO = 390
        print("We have Top 3 games")
        print("-------------------------------------------")
        print("1: PUBG = 590THB")
        print("2: DBDL = 590THB")
        print("3: CSGO = 390THB")
        print("-------------------------------------------")
        print(">>if you want buy only PUBG Press >> 1")
        print(">>if you want buy only DBDL Press >> 2")
        print(">>if you want buy only CSGO Press >> 3")
        print(">>if you want buy PUBG and DBDL Press >> 4")
        print(">>if you want buy PUBG and CSGO Press >> 5")
        print(">>if you want buy DBDL and CSGO Press >> 6")
        print(">>if you want buy ALL Press >>7")
        Game = int(input("Press Here :"))
        if Game == 1:
            print("You want to buy only PUBG :D")
            many = int(input("How many do you want to buy:"))
            print("PUBG :",PUBG,"x",many,"=",PUBG*many,"THB")
        elif Game == 2:
            print("You want to buy only DBDL :D")
            many = int(input("How many do you want to buy:"))
            print("DBDL :" ,DBDL,"x",many,"=",DBDL*many,"THB")
        elif Game == 3:
            print("You want to buy only CSGO :D")
            many = int(input("How many do you want to buy:"))
            print("CSGO :",CSGO,"x",many,"=",CSGO*many,"THB")
        elif Game == 4:
            print("You want to buy PUBG and DBDL :D")
            many = int(input("How many do you want to buy:"))
            print("PUBG and DBDL :","(",PUBG,"+",DBDL,")","x",many,"=",(PUBG+DBDL)*many,"THB")
        elif Game == 5:
            print("You want to buy PUBG and CSGO :D")
            many = int(input("How many do you want to buy:"))
            print("PUBG and CSGO :","(",PUBG,"+",CSGO,")","x",many,"=",(PUBG+CSGO)*many,"THB")
        elif Game == 6:
            print("You want to buy DBDL and CSGO :D")
            many = int(input("How many do you want to buy:"))
            print("DBDL and CSGO :","(",DBDL,"+",CSGO,")","x",many,"=",(DBDL+CSGO)*many,"THB")
        elif Game == 7:
            print("You want to buy ALL :D")
            many = int(input("How many do you want to buy:"))
            print("PUBG and DBDL and CSGO :","(",PUBG,"+",DBDL,"+",CSGO,")","x",many,"=",(PUBG+DBDL+CSGO)*many,"THB")
        else:
            print("See ypu later")
        print("-------------Thank You!!------------")
    elif Choice == 2:
        CPU = 10600
        VPU = 35600
        RAM = 2590
        CPU1 = "CPU corei7 7700K"
        VPU1 = "Geford RTX 2080"
        RAM1 = "Kingston DDR4/2400 16GB(8x2)"
        print("We have only CPU,VPU,RAM in stock")
        print("----------------------------------")
        print("1: CPU corei77700K = 10600THB")
        print("2: Geford RTX 2080 = 35600THB")
        print("3: Kingston DDR4/2400 16GB(8x2) = 2590THB")
        print("----------------------------------")
        print(">>if you want buy only CPU Press >> 1")
        print(">>if you want buy only VPU Press >> 2")
        print(">>if you want buy only RAM Press >> 3")
        print(">>if you want buy CPU and VPU Press >> 4")
        print(">>if you want buy CPU and RAM Press >> 5")
        print(">>if you want buy VPU and RAM Press >> 6")
        print(">>if you want buy ALL Press >> 7")
        Hardware = int(input("Press Here :"))
        if Hardware == 1:
            print("You want to buy only CPU :D")
            many = int(input("How many do you want to buy:"))
            print(CPU1,":",CPU,"x",many,"=",CPU*many,"THB")
        elif Hardware == 2:
            print("You want to buy only VPU :D")
            many = int(input("How many do you want to buy:"))
            print(VPU1,":",VPU,"x",many,"=",VPU*many,"THB")
        elif Hardware == 3:
            print("You want to buy only RAM :D")
            many = int(input("How many do you want to buy:"))
            print(RAM1,":", RAM,"x",many,"=",RAM*many,"THB")
        elif Hardware == 4:
            print("You want to buy CPU and VPU :D")
            many = int(input("How many do you want to buy:"))
            print(CPU1,"and",VPU1,":","(", CPU,"+",VPU,")","x",many,"=",(CPU+VPU)*many,"THB")
        elif Hardware == 5:
            print("You want to buy CPU and RAM :D")
            many = int(input("How many do you want to buy:"))
            print(CPU1,"and",RAM1,":","(",CPU,"+",RAM,")","x",many,"=",(CPU+RAM)*many,"THB")
        elif Hardware == 6:
            print("You want to buy VPU and RAM :D")
            many = int(input("How many do you want to buy:"))
            print(VPU1, "and",RAM1,":","(",VPU,"+",RAM,")","x",many,"=",(VPU+RAM)*many,"THB")
        elif Hardware == 7:
            print("You want to buy ALL :D")
            many = int(input("How many do you want to buy:"))
            print(CPU1,"and",VPU1,"and",RAM1,":","(",CPU,"+",VPU,"+",RAM,")","x",many,"=",(CPU+VPU+RAM)*many,"THB")
        else:
            print("See you later")
        print("-------------Thank You!!------------")
    elif Choice == 3:
        PHS = 1290
        LR = 1390
        Pre = 1490
        PHS1 = "Photoshop 2019"
        LR1 = "Lightroom 2019"
        Pre1 = "Premiere Pro 2019"
        print("We have PHS 2019,LR 2019,Premiere Pro 2019")
        print("-------------------------------------")
        print("1: Photoshop 2019 = ")
        print("2: Lightroom 2019 = ")
        print("3: Premiere Pro 2019")
        print("-------------------------------------")
        print(">>if you want buy only PHS 2019 Press >> 1")
        print(">>if you want buy only LR 2019 Press >> 2")
        print(">>if you want buy only Premiere Pro 2019 Press >> 3")
        print(">>if you want buy PHS and LR Press >> 4")
        print(">>if you want buy PHS and Pre Press >> 5")
        print(">>if you want buy LR and Pre Press >> 6")
        print(">>if you want buy ALL Press >> 7")
        Sofeware = int(input("Press Here :"))
        if Sofeware == 1:
            print("You want to buy only PHS 2019 :D")
            many = int(input("How many do you want to buy:"))
            print(PHS1,":",PHS,"x",many,"=",PHS*many,"THB")
        elif Sofeware == 2:
            print("You want to buy only LR 2019 :D")
            many = int(input("How many do you want to buy:"))
            print(LR1,":",LR,"x",many,"=",LR*many,"THB")
        elif Sofeware == 3:
            print("You want to buy only Premiere Pro 2019 :D")
            many = int(input("How many do you want to buy:"))
            print(Pre1,":",Pre,"x",many,"=",Pre*many,"THB")
        elif Sofeware == 4:
            print("You want to buy PHS and LR :D")
            many = int(input("How many do you want to buy:"))
            print(PHS1,"and",LR1,":","(",PHS,"+",LR,")","x",many,"=",(PHS+LR)*many,"THB")
        elif Sofeware == 5:
            print("You want to buy PHS and Pre :D")
            many = int(input("How many do you want to buy:"))
            print(PHS1,"and",Pre1,":","(",PHS,"+",Pre,")","x",many,"=",(PHS+Pre)*many,"THB")
        elif Sofeware == 6:
            print("You want to buy LR and Pre :D")
            many = int(input("How many do you want to buy:"))
            print(LR1,"and",Pre1,":","(",LR,"+",Pre,")","x",many,"=",(LR+Pre)*many,"THB")
        elif Sofeware == 7:
            print("You want to buy ALL :D")
            many = int(input("How many do you want to buy:"))
            print(PHS1,"and",LR1,"and",Pre1,":","(",PHS,"+",LR,"+",Pre,")","x",many,"=",(PHS+LR+Pre)*many,"THB")
        else:
            print("See you later")
        print("-------------Thank You!!------------")
else:
    print("Username or Password incorrect!!")
