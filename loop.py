# i=10
# while i>=0:
#     print(i)
#     i-=1
# i=0
# odd=[]
# while i<=100:
    
#     if i%2!=0:
#      odd.append(i)
#     i+=1
# print(f"Total number of even number from 0 to 100 is :{len(odd)}")  

# data= [
#     [12,45,52,52,63],
#     [52,25,25,36,25],
#     [98,63,54,25,52]
# ]
# for a in data:
#     for b in a:
#         print(b)
#     print()
# a=int(input("Enter the number to check the multiply"))
# i=1
# while i<=10:
#     z=a*i
#     print(z)
#     i+=1
number= int(input("Enter the number of student : \n"))
student_marks=[]
x=1 
while x<=number:
    print(f"Enter the marks of {x} Student")
    for i in range(1):
        nep=int(input("Enter the marks of nepali:"))
        eng=int(input("Enter the marks of English:"))
        math=int(input("Enter the marks of math:"))
        science=int(input("Enter the marks of science:"))
        popula=int(input("Enter the marks of popula :"))
        total=nep+eng+math+science+popula
        student_marks.append(total)
    x+=1

for total in student_marks:
    per=total/5
    grade=" "
    if per>=80:
        grade="A"
    elif per>=60 and per<80:
        grade="B"
    elif per>=40 and per<60:
            grade="C"
    else:
        grade="D"
print(f"Total number of student is {number}")
print(f"Total number of student is {len(student_marks)}")





