import datetime

# jobs = [
#     {'title': 'python developer', 'salary': 1000, 'exp_date': '2021-03-01'},
#     {'title': 'java developer', 'salary': 1100, 'exp_date': '2024-05-02'},
#     {'title': 'c# developer', 'salary': 111000, 'exp_date': '2022-03-01'},
#     {'title': 'c++ developer', 'salary': 1300, 'exp_date': '2031-03-01'}
# ]

# for i, job in enumerate(jobs, start=1):
#     print(f"{i}. The job is: {job['title']}")

# option = int(input("Enter a job to check: "))
# selected_job = jobs[option - 1]

# exp_date = datetime.datetime.strptime(selected_job['exp_date'], '%Y-%m-%d')
# if exp_date < datetime.datetime.now():
#     print(f"{selected_job['title']} is expired")
# else:
#     print(f"{selected_job['title']} is not expired")
#     ask = input("Do you want to extend the date time? ")
#     if ask.lower() == "yes":
#         selected_job['exp_date'] = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')
#         print(f"New expiration date for {selected_job['title']}: {selected_job['exp_date']}")



goods=[
    {'title':'Biscits','md':'2024-07-24'},
    {'title':'Bread','md':'2024-05-24'},
    {'title':'Milk','md':'2023-12-24'},
    {'title':'Eggs','md':'2021-07-24'}
]
for i, good in enumerate(goods,start=1):
    print(f"{i}. {good['title']}")
    time=datetime.datetime.strptime(good['md'],'%Y-%m-%d')
    dur=datetime.datetime.now()-time
    rem=dur.days/30 
    if rem<6:
        print(f"{good['title']} is new")
    elif rem>6 and rem<=12:
        print(f"{good['title']} is old")
    else:
        print(f"{good['title']} is expired")