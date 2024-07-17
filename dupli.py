# data=['ram','sita','ram','hari','laxmi','laxmi']
# print(data)
# h=set(data) # set(listsname) to remove the duplicate code

# students = [
#     {'name': 'ram', 'gender': 'male', 'status': True},
#     {'name': 'sita', 'gender': 'female', 'status': False},
#     {'name': 'hari', 'gender': 'male', 'status': True},
#     {'name': 'laxmi', 'gender': 'female', 'status': True},
#     {'name': 'gopal', 'gender': 'male', 'status': False}
# ]
# total_active_user=0
# total_inactive_user=0
# total_male=0
# total_female=0

# total_active_female=0
# total_active_male=0
# total_inactive_female=0
# total_inactive_male=0

# i=0
# print(f"Total number of users: {len(students)}")
# while i<len(students):
#     if students[i]['status']==True:
#         total_active_user+=1
#         if students[i]['gender']=='male':
#             total_male+=1
#             total_active_male+=1
#         elif students[i]['gender']=='female':
#             total_female+=1
#             total_active_female+=1

    
#     elif students[i]['status']==False:
#         total_inactive_user+=1
#         if students[i]['gender']=='male':
#             total_male+=1
#         else:
#             total_female+=1
#         if students[i]['gender']=='male':
#             total_male+=1
#             total_inactive_male+=1
#         elif students[i]['gender']=='female':
#             total_female+=1
#             total_inactive_female+=1
#     i+=1
# print(f"Total number of active user is :{total_active_user}")
# print(f"Total number of active user is :{total_inactive_user}")
# print(f"Total male is :{total_male}")
# print(f"Total female is :{total_female}")
# print(f"Total active male is :{total_active_male}")
# print(f"Total active female is :{total_active_female}")
# print(f"Total active male is :{total_inactive_male}")
# print(f"Total active female is :{total_inactive_female}")
users=[
    {'username':'ram','password':'ram002'},
    {'username':'sita','password':'sita002'},
    {'username':'hari','password':'hari002'},
   
]

books =[
    {'name':'book1','author':'author1','price':100},
    {'name':'book2','author':'author2','price':200},
    {'name':'book3','author':'author3','price':300},
]

username=input("Enter the username : \n ")
password=input("Enter the password : \n ")

for user in users: 
    if username==user['username'] and password==user['password']:
        print("Login Successfull")
        boo=input("Enter the name of  book: \t")
        for book in books:
            
            if book['name']==boo:
                print("Book is available")
                print(f"Book name is :{book['name']}")
                print(f"Book author is :{book['author']}")
                print(f"Book price is :{book['price']}")
                


        break
    else:
        print("Incorrect password or username")
        break
    
      
    

        











    


