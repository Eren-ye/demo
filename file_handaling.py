# object=open("users.txt","a")
# object.write("username:eren\n")
# object.close()

# inp=input("Enter the name :")
# em=input("Enter the email :")
# p=int(input("Enter the phone :"))
# add=input("Enter the address")

# stor=open("Store.txt","a")
# stor.write(f"username: {inp}\n")
# stor.write(f"email: {em}\n")
# stor.write(f"Phone no {p} \n")
# stor.write(f"Address: {add} \n ")
# stor=open("Store.txt","r")
# print(stor.read())
# stor.close()
# marks=open("Store.txt","a")
# number= int(input("Enter the number of student : \n"))

# x=1 
# while x<=number:
#     print(f"Enter the marks of {x} Student")
#     for i in range(number+1):
#         nep=int(input("Enter the marks of nepali:"))
#         eng=int(input("Enter the marks of English:"))
#         math=int(input("Enter the marks of math:"))
#         science=int(input("Enter the marks of science:"))
#         popula=int(input("Enter the marks of popula :"))
#         marks.write(f" Score in nepali is :{nep} \n")
#         marks.write(f" Score in English is :{eng} \n")
#         marks.write(f" Score in math is :{math} \n")
#         marks.write(f" Score in science is :{science} \n")
#         marks.write(f" Score in popula is :{popula} \n")
#         marks.close()
        
#     x+=1

# score=[]
# num=int(input("Enter the number of students :"))
# for i in range(num):
#     print(f"Enter the marks of {i} student")
#     marks={
#     'nep':int(input("Enter the marks of nepali: \n")),
#     'eng':int(input("Enter the marks of English: \n ")),
#     'math':int(input("Enter the marks of math: \n"))
#     }
#     score.append(marks)
# stor=open("Store.txt","a")
# for i in score:
#     stor.write(f" Score in nepali is :{i['nep']} \n")
#     stor.write(f" Score in english is :{i['eng']}\n")
#     stor.write(f" Score in math is :{i['math']}\n")
    

# stor=open("Store.txt","r")
# print(stor.read())

print("=============MOBILE============")
print("1.SAMSUNG(RS45,000) \n 2.IPHONE(RS60000) \n 3.POCO(20000) \n 4.ROG(10005)")
samsung_price=0
iphone_price=0
poco_price=0
rog_price=0
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

total_price=(total_price*100)/13
print("============BILL========")
print(f"YOU HAVE SELECTED THE: {ph}")
print(f" YOUR DELEVERY CHARGES IS: {ch}")
print(f"YOUR COVER IS : {co}")
print(f"YOUR LOCATION IS: {loc}")
print(" YOU NEED TO PAY TOTAL 13% EXTRA AS TAX ")
print("Total Price : ",total_price)
offical=open("LAptop.txt","a")
offical.write(f"The phone is :{ph}\n")
offical.write(f"THE DELIVERY CHARGES IS :{ch} \n")
offical.write(f"The cover is :{co}\n")
offical.write(f"The location is :{loc}\n")
offical.write(f"THE TOTAL PRICE IS :{total_price}\n")
offical=open("LAptop.txt","r")
print(offical.read())
 



    






