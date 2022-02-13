
from lifestore_file import lifestore_sales, lifestore_products, lifestore_searches
#Productos por categorías
product_categories= {}

for element in lifestore_products:
    category = element[3]
    product = element[1]
    id = element[0]
    if category not in product_categories.keys():
        product_categories[category] = {}
        if 'items' not in product_categories[category].keys():
            product_categories[category]['items'] = []
    product_categories[category]['items'].append([product,id])
    


#Info productos por index
def index_inventory():
    index_inventory = {}
    for element in lifestore_products:
        id_in = element[0]
        name_in = element[1]
        price_in = element[2]
        category_in = element[3]
        stock_in = element[4]
        if id_in not in index_inventory.keys():
            index_inventory[id_in] = {} 
            if 'name' not in index_inventory[id_in].keys():
                index_inventory[id_in]['name'] = name_in
            if 'price' not  in index_inventory[id_in].keys():
                index_inventory[id_in]['price'] = price_in
            if 'category' not  in index_inventory[id_in].keys():
                index_inventory[id_in]['category'] = category_in
            if 'stock' not  in index_inventory[id_in].keys():
                index_inventory[id_in]['stock'] = stock_in
            else:
                continue
    return index_inventory
inventory = index_inventory()
#Ventas por categoría 
def sales4_cat():
    for element in lifestore_sales:
        id = element[1]
        if element[4] == 1:
            refund = True
        else:
            refund = False
        for key in product_categories.keys():
            if 'sales' not in product_categories[key].keys():
                product_categories[key]['sales'] = []
            for product in product_categories[key]['items']:
                if id == product[1]:
                    product_categories[key]['sales'].append(inventory[id]['price'])
    return
sales4_cat()
def search4_cat():
    for element in lifestore_searches:
        id = element[1]
        for category in product_categories.keys():
            if 'searches' not in product_categories[category].keys():
                product_categories[category]['searches'] = []
            for product in product_categories[category]['items']:
                if id ==product[1]:
                    product_categories[category]['searches'].append(id)
    return
search4_cat()

# for key in product_categories.keys():
#     print(f'\n {key}:')
#     for product in product_categories[key]['items']:
#         print(f'\t {product[0]} - id {product[1]}')
#     venta_cat = sum(product_categories[key]['sales'])
#     venta_prom_cat = venta_cat/len(product_categories[key]['items'])
#     searched = len(product_categories[key]['searches'])
#     print(f'\n \t Ventas total: ${venta_cat}.00 MXN')
#     print(f'\t Ventas promedio: ${venta_prom_cat}.00 MXN')
#     print(f'\n \t Total de búsquedas: {searched}')

#Categoria vs ventas
cat = product_categories.keys()
ventas_tot = [sum(product_categories[key]['sales']) for key in cat ]
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.ticker as ticker

fig, ax = plt.subplots()

ax.plot(cat, ventas_tot)
ax.grid()
ax.set_xlabel('Categoría de producto')
ax.set_ylabel('Ventas totales') 
ax.set_xticklabels(cat, rotation=45)
ax.set_yticklabels(ventas_tot, rotation=0)
ax.set_title('Ventas por categoría')
formatter = ticker.FormatStrFormatter('$%1.2f')
ax.yaxis.set_major_formatter(formatter)

for tick in ax.yaxis.get_major_ticks():
    tick.label1.set_visible(False)
    tick.label2.set_visible(True)
    tick.label2.set_color('green')
