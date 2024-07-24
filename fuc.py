# def add(x,y):
#     print(f"Sum is: {x+y}")

# def sub(x,y):
#     print(f"sub is: {x+y}")

# def mul(x,y):
#     print(f"mul is: {x+y}")

# add(50,60)
# sub(50,30)
# mul(20,30)
# def marksheet(ma,sc,nep,com):
#     print(f"Total is : {ma+sc+nep+com}")
#     per=(ma+sc+nep+com)*100/120
#     print(f" Total percentage is :{per}")
#     grade=" "
#     if per>=80:
#         grade="A"
#     elif per>=60 and per<80:
#         grade="B"
#     elif per>=40 and per<60:
#             grade="C"
#     else:
#         grade="D"
# marksheet(10,20,30,10)
# def input_value():
#     nep=int(input(" Enter the value :"))
#     ma=int(input(" Enter the value :"))
#     sc=int(input(" Enter the value :"))
#     com=int(input(" Enter the value :"))
#     return [nep,ma,sc, com]

# def ccal():
#     nep,ma,sc,com=input_value()
#     total=nep+ma+sc+com
#     return total

# print(ccal())
 

def options():
    print("=============MOBILE============") 
    print("1.SAMSUNG(RS45,000) \n 2.IPHONE(RS60000) \n 3.POCO(20000) \n 4.ROG(10005)")


def select():
   
    total_price=0
    option= int(input("Enter the option"))
    ph=" "
    if option==1:
        print("You have selected the Samsung phone")
        ph="SAMSUNG"
        samsung_price=45000
    elif option==2:
        print("You have selected the iPhone phone")
        ph="Iphone"
        iphone_price=60000
    elif option==3:
        print("You have selected the Poco phone")
        ph="POCO"
        poco_price=20000
    elif option==4:
        print("You have selected the ROG phone")
        ph="ROG"
        rog_price=10005
    else:
        print(" INVALID OPTION")
        exit()
    return [ph,total_price]

def deli():
    total_price=select()
    samsung_price=0
    iphone_price=0
    poco_price=0
    rog_price=0
    delivery=int(input("Enter the deleivery option : \n  1.BY BIKE(2000) \n 2. HOME DELIVERY(1000)  \n 3.PICK FROM THE STORE(500) \n"))
    ch=" "
    if delivery==1:
        print("You have selected the bike delivery")
        total_price=samsung_price+2000
        ch="RS2000"

    elif delivery==2:
        print("You have selected the home delivery")
        total_price=samsung_price+1000
        ch="1000"
    elif delivery==3:
        print("You have selected the pick from the store")
        total_price=samsung_price+500
        ch="500"
    else:
        print("INVALID OPTION")
        exit()
    
    return [ch,total_price]


def wra():
    total_price=deli()
    wrapp=int(input(" HOW DO YOU WANT TO WRAP YOUR DEVICE : \n 1.BY PLASTIC(200) \n 2.BY PAPER(100) \n 3. NOTHING(0) \n"))
    co=" "
    if wrapp==1:
        print("You have selected the plastic wrap")
        total_price=total_price+200
        co=" PLASTIC"
    elif wrapp==2:
        print("You have selected the paper wrap")
        total_price=total_price+100
        co="PAPER"
    elif wrapp==3:
        print("You have selected the nothing")

    else:
        print("INVALID OPTION")
        co="NOTHING"
        exit()
    return [total_price,co]

def loca():
    location=int(input("Enter your location : \n 1.INSIDE KTM(0) \n 2.INSIDE LALITPUR(0) \n 3. OUTSIDE THE VALLEY(RS2000) \n "))
    loc=" "
    if location==1:
            print("You have selected the inside KTM")
            loc="KTM"
    elif location==2:
        print(" You have selected the lalitpur")
        loc="LALITPUR"
    else:
        print("You have selected the outside the valley")
        total_price=total_price+2000
    loc=" outside the valley"
    exit()
    return [total_price,loc]

def display():
    total_price,loc=loca()
    co=wra()
    ph=select()
    total_price=(total_price*18/100)+total_price
    ch,price=deli()
    print(options())
    print(select())
    print(deli())
    print(wra())
    print(loca())
    print(" You have selected the",ph)
    print("Your device is wrapped by ",co)
    print("Your device is located at ",loc)
    print(f"In toal the 18% tax will be also included:{(total_price*18/100)}")
    print("Your total price is : ",total_price)
    display()