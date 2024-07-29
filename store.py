import os 
if not os.path.exists('data.txt'):
    cr=open('data.txt','a')
    cr.close()

print("=============MOBILE============")
print("1.SAMSUNG(RS45,000) \n 2.IPHONE(RS60000) \n 3.POCO(20000) \n 4.ROG(10005)")
samsung_price=0
iphone_price=0
poco_price=0
rog_price=0
total_price=0
option= int(input("Enter the option").strip())
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

delivery=int(input("Enter the deleivery option : \n  1.BY BIKE(2000) \n 2. HOME DELIVERY(1000)  \n 3.PICK FROM THE STORE(500) \n").strip())
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

wrapp=int(input(" HOW DO YOU WANT TO WRAP YOUR DEVICE : \n 1.BY PLASTIC(200) \n 2.BY PAPER(100) \n 3. NOTHING(0) \n").strip())
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
location=int(input("Enter your location : \n 1.INSIDE KTM(0) \n 2.INSIDE LALITPUR(0) \n 3. OUTSIDE THE VALLEY(RS2000) \n ").strip())
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

total_price=(total_price*100)/13



def store():
    with open('data.txt','a') as file:
        file.write(f"Selected:{ph},Delivery Charges:{ch},Cover:{co},Location:{loc},Total price:{total_price} \n")
        print("Thank You !")



store()

def shows():
    with open('data.txt','r') as file:
        show=file.readlines()
        for show in show:
            sho=show.strip().split(",")
            print(sho[0].split(":")[1])
            print(sho[1].split(":")[1])
            print(sho[2].split(":")[1])
            print(sho[3].split(":")[1])
            print(sho[4].split(":")[1])
           
shows()