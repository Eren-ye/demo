# print("=============MOBILE============")
# print("1.SAMSUNG(RS45,000) \n 2.IPHONE(RS60000) \n 3.POCO(20000) \n 4.ROG(10005)")
# samsung_price=0
# iphone_price=0
# poco_price=0
# rog_price=0
# total_price=0
# option= int(input("Enter the option"))
# ph=" "
# if option==1:
#     print("You have selected the Samsung phone")
#     ph="SAMSUNG"
#     samsung_price=45000
# elif option==2:
#     print("You have selected the iPhone phone")
#     ph="Iphone"
#     iphone_price=60000
# elif option==3:
#     print("You have selected the Poco phone")
#     ph="POCO"
#     poco_price=20000
# elif option==4:
#     print("You have selected the ROG phone")
#     ph="ROG"
#     rog_price=10005
# else:
#     print(" INVALID OPTION")
#     exit()

# delivery=int(input("Enter the deleivery option : \n  1.BY BIKE(2000) \n 2. HOME DELIVERY(1000)  \n 3.PICK FROM THE STORE(500) \n"))
# ch=" "
# if delivery==1:
#     print("You have selected the bike delivery")
#     total_price=samsung_price+2000
#     ch="RS2000"

# elif delivery==2:
#     print("You have selected the home delivery")
#     total_price=samsung_price+1000
#     ch="1000"
# elif delivery==3:
#     print("You have selected the pick from the store")
#     total_price=samsung_price+500
#     ch="500"
# else:
#     print("INVALID OPTION")
#     exit()

# wrapp=int(input(" HOW DO YOU WANT TO WRAP YOUR DEVICE : \n 1.BY PLASTIC(200) \n 2.BY PAPER(100) \n 3. NOTHING(0) \n"))
# co=" "
# if wrapp==1:
#     print("You have selected the plastic wrap")
#     total_price=total_price+200
#     co=" PLASTIC"
# elif wrapp==2:
#     print("You have selected the paper wrap")
#     total_price=total_price+100
#     co="PAPER"
# elif wrapp==3:
#     print("You have selected the nothing")

# else:
#     print("INVALID OPTION")
#     co="NOTHING"
#     exit()
# location=int(input("Enter your location : \n 1.INSIDE KTM(0) \n 2.INSIDE LALITPUR(0) \n 3. OUTSIDE THE VALLEY(RS2000) \n "))
# loc=" "
# if location==1:
#     print("You have selected the inside KTM")
#     loc="KTM"
# elif location==2:
#     print(" You have selected the lalitpur")
#     loc="LALITPUR"
# else:
#     print("You have selected the outside the valley")
#     total_price=total_price+2000
#     loc=" outside the valley"
#     exit()

# total_price=(total_price*100)/13
# print("============BILL========")
# print(f"YOU HAVE SELECTED THE: {ph}")
# print(f" YOUR DELEVERY CHARGES IS: {ch}")
# print(f"YOUR COVER IS : {co}")
# print(f"YOUR LOCATION IS: {loc}")
# print(" YOU NEED TO PAY TOTAL 13% EXTRA AS TAX ")
# print("Total Price : ",total_price)
#  100 min, 1-10 ntc-ntc ->2.5 , ntc-ncl 3.5 , ncl-ncl-5 ncl-ntc ->4

print(" Select the SIM option ")
select=int(input(" 1) NTC-NTC \n 2) NTC-NCL \n 3) NCL-NTC \n 4)NCL-NCL \n"))  
dur=int(input(" Enter the time duration of phone call "))

if select==1:
    print(" You have selected the NTC-NTC")
    if dur>=0 and dur<=10:
        print(" Your total is 2.5")
    elif dur>10 and dur<=20:
        print(f" Your total is {2.5*2}")
    elif dur>20 and dur<=30:
        print(f" Your total is {2.5*3}")
    elif dur>30 and dur<=40:
        print(f" Your total is {2.5*4}")
    elif dur>40 and dur<=50:
        print(f" Your total is {2.5*5}")
    elif dur>50 and dur<=60:
        print(f" Your total is {2.5*6}")
    elif dur>60 and dur<=70:
        print(f" Your total is {2.5*7}")
    elif dur>70 and dur<=80:
        print(f" Your total is {2.5*8}")
    elif dur>80 and dur<=90:
        print(f" Your total is {2.5*9}")
    elif dur>90 and dur<=100:
        print(f" Your total is {2.5*10}")
    else:
        print("INVALID")
elif select==2:
    print(" You have selected the NTC-NCL")
    if dur>=0 and dur<=10:
        print(" Your total is 3.5")
    elif dur>10 and dur<=20:
        print(f" Your total is {3.5*2}")
    elif dur>20 and dur<=30:
        print(f" Your total is {3.5*3}")
    elif dur>30 and dur<=40:
        print(f" Your total is {3.5*4}")
    elif dur>40 and dur<=50:
        print(f" Your total is {3.5*5}")
    elif dur>50 and dur<=60:
        print(f" Your total is {3.5*6}")
    elif dur>60 and dur<=70:
        print(f" Your total is {3.5*7}")
    elif dur>70 and dur<=80:
        print(f" Your total is {3.5*8}")
    elif dur>80 and dur<=90:
        print(f" Your total is {3.5*9}")
    elif dur>90 and dur<=100:
        print(f" Your total is {3.5*10}")
    else:
        print("INVALID")
elif select==3:
    print(" You have selected the NCL-NTC")
    if dur>=0 and dur<=10:
        print(" Your total is 4")
    elif dur>10 and dur<=20:
        print(f" Your total is {4*2}")
    elif dur>20 and dur<=30:
        print(f" Your total is {4*3}")
    elif dur>30 and dur<=40:
        print(f" Your total is {4*4}")
    elif dur>40 and dur<=50:
        print(f" Your total is {4*5}")
    elif dur>50 and dur<=60:
        print(f" Your total is {4*6}")
    elif dur>60 and dur<=70:
        print(f" Your total is {4*7}")
    elif dur>70 and dur<=80:
        print(f" Your total is {4*8}")
    elif dur>80 and dur<=90:
        print(f" Your total is {4*9}")
    elif dur>90 and dur<=100:
        print(f" Your total is {4*10}")
    else:
        print("INVALID")
elif select==4:
    print(" You have selected the NCL-NCL")
    if dur>=0 and dur<=10:
        print(" Your total is 5")
    elif dur>10 and dur<=20:
        print(f" Your total is {5*2}")
    elif dur>20 and dur<=30:
        print(f" Your total is {5*3}")
    elif dur>30 and dur<=40:
        print(f" Your total is {5*4}")
    elif dur>40 and dur<=50:
        print(f" Your total is {5*5}")
    elif dur>50 and dur<=60:
        print(f" Your total is {5*6}")
    elif dur>60 and dur<=70:
        print(f" Your total is {5*7}")
    elif dur>70 and dur<=80:
        print(f" Your total is {5*8}")
    elif dur>80 and dur<=90:
        print(f" Your total is {5*9}")
    elif dur>90 and dur<=100:
        print(f" Your total is {5*10}")
    else:
        print("INVALID")


