from business.customerBS import CustomerBS
from business.productBS import ProductBS
from business.storeHouseBS import StoreHouseBS
from entities.customer import Customer

# ---------- customer ---------------

customer = CustomerBS()
List = customer.findAll()
for item in List:
    print('id = ', item.id, end=' , ')
    print('name = ', item.name, end=' , ')
    print('town = ', item.town, end=' , ')
    print('balance = ', item.balance, end=' , ')
    print('governrate = ', item.governrate, end=' , ')
    print('salesperson_id = ', item.salesperson_id, end=' , ')
    print('street_number = ', item.street_number)

print()

item = customer.findById(3)
print('id = ', item.id, end=' , ')
print('name = ', item.name, end=' , ')
print('town = ', item.town, end=' , ')
print('balance = ', item.balance, end=' , ')
print('governrate = ', item.governrate, end=' , ')
print('salesperson_id = ', item.salesperson_id, end=' , ')
print('street_number = ', item.street_number)

print()

# ---------- product ---------------

product = ProductBS()
List = product.findAll()
for item in List:
    print('id = ', item.id, end=' , ')
    print('price = ', item.price, end=' , ')
    print('desc = ', item.desc, end=' , ')
    print('product_class = ', item.product_class)

print()

item = product.findById(2)
print('id = ', item.id, end=' , ')
print('price = ', item.price, end=' , ')
print('desc = ', item.desc, end=' , ')
print('product_class = ', item.product_class)

print()

# ---------- storeHouse ---------------

storeHouse = StoreHouseBS()
List = storeHouse.findAll()
for item in List:
    print('number = ', item.number, end=' , ')
    print('place = ', item.place)

print()

item = storeHouse.findById(2)
print('number = ', item.number, end=' , ')
print('place = ', item.place)

print()
