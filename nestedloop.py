categoryData=[
    {'id':1,'name':'laptop'},
    {'id':2,'name':'mobile'},
    {'id':3,'name':'tablet'}
]

productData=[
    {'id':1,'name':'dell','category_id':1},
    {'id':2,'name':'mac','category_id':1},
    {'id':3,'name':'iphone','category_id':2},
    {'id':4,'name':'samsung','category_id':2},
    {'id':5,'name':'ipad','category_id':3},
    {'id':6,'name':'samsung tab','category_id':3}
]

for category in categoryData:
    print(f"========={category['name']}=========")
    for product in productData:
        if category['id']==product['category_id']:
            print('\t',product['name'])
categories = [
    {'id': 1, 'name': 'Classic'},
    {'id': 2, 'name': 'Dirt'},
    {'id': 3, 'name': 'Naked'}
]

products = [
    {'id': 1, 'name': 'RR', 'data': 1,'price':50000},
    {'id': 2, 'name': 'JAWA', 'data': 1,'price':80000},
    {'id': 3, 'name': 'CRX', 'data': 2 ,'price':79999},
    {'id': 4, 'name': 'Asina', 'data': 2, 'price':49999},
    {'id': 5, 'name': 'NS', 'data': 3,'price':43750},
    {'id': 6, 'name': 'Taro', 'data': 3,'price':75000},
    {'id':7, 'name':'Royal Enfield Meteor','data':1,'price':55000},
    {'id':9, 'name':'Honda CRF250L','data':2, 'price':1250000},
    {'id':10, 'name':'KTM 450 EXC-F','data':2, 'price':1600000},
    {'id':11, 'name':'Benelli Imperiale 400','data':3, 'price':760000},
    {'id':12, 'name':'KTM Duke 200','data':3, 'price':540000}


]


sorted_products = sorted(products, key=lambda x: x['name'])


for category in categories:
    print(f"========== {category['name']} ============")
    for product in sorted_products:
        if product['data'] == category['id']:
            print(f"\t{product['name']} with a price tag of {product['price']}")

type_input = input("Enter the type: \n")

quantatiy=0
for category in categories:
    if category['name'] == type_input:
        print(f"========== {category['name']} ============")
        for product in sorted_products:
            if product['data'] == category['id']:
                print(f"\t{product['name']}")
item=input("Enter the name of the product : \t ")
for product in sorted_products:
   if product['name'] == item:
       print(f" You have selected {product['name']} with a price tag of {product['price']}")
       rate=product['price']

quantatiy=int(input("Enter the quantatiy of the products : \t"))
if quantatiy>0 and quantatiy<=10:
    total_price=rate*quantatiy
    print(f"Total price is : {total_price}")




