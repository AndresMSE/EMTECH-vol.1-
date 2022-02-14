
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
                product_categories[key]['sales'] = [[],[]]
            for product in product_categories[key]['items']:
                if id == product[1]:
                    product_categories[key]['sales'][0].append(inventory[id]['price'])
                    product_categories[key]['sales'][1].append(id)
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
#     venta_cat = sum(product_categories[key]['sales'][0])
#     venta_prom_cat = venta_cat/len(product_categories[key]['items'])
#     searched = len(product_categories[key]['searches'])
#     print(f'\n \t Ventas total: ${venta_cat}.00 MXN')
#     # print(f'\t Ventas promedio: ${venta_prom_cat}.00 MXN')
#     print(f'\n \t Total de búsquedas: {searched}')

#Categoria vs ventas
cat = product_categories.keys()
ventas_tot = [sum(product_categories[key]['sales'][0]) for key in cat ]

def gen_minsales(sales):
    min_sales = sorted(sales)
    best_sold_prod_cat = {}
    for  min in min_sales:
        for category in product_categories.keys():
            if sum(product_categories[category]['sales'][0]) == min:
                if category not in best_sold_prod_cat.keys():
                    best_sold_prod_cat[category] = {}
                for prod in product_categories[category]['items']:
                    if prod[1] not in best_sold_prod_cat[category].keys():
                        best_sold_prod_cat[category][prod[1]] = product_categories[category]['sales'][1].count(prod[1])
    return best_sold_prod_cat
print(gen_minsales(ventas_tot))      
def get_minsales(diction):
    worst_cat =[]    
    worst_products = {}
    for category in diction.keys():
        worst_cat.append(category)
    for category in diction.keys():
        aux = []
        for product in diction[category].keys():
            aux.append(diction[category].get(product))
        aux.sort()
        for productval in aux:
            for product in diction[category].keys():
                if category not in worst_products.keys():
                    worst_products[category] = []
                if productval == diction[category].get(product):
                    name = inventory[product]['name']
                    worst_products[category].append(product)
    return worst_products,worst_cat

least5_prod, least5_cat = get_minsales(gen_minsales(ventas_tot))

print('Las peores categorías son:')
for k in range(len(least5_cat)):
    print(f'\t {k+1}: {least5_cat[k]}')
    print(f'\t Donde los 5 productos menos vendidos son:')
    for lprod in least5_prod[least5_cat[k]][0:5]:
        name = inventory[lprod]['name']
        print(f'\t \t{name} ')



# search_minsales(ventas_tot)

# def search_maxsales(sales):
#     max_sales = sorted(sales, reverse=True)[0]
#     for category in product_categories.keys():
#         if sum(product_categories[category]['sales']) == max_sales:
#             return print(f'\n La categoría con mayores ventas es {category}')
#         else:continue
# search_maxsales(ventas_tot)

# busqueda_tot = [ len(product_categories[key]['searches']) for key in cat]
# def search_minsearch(search):
#     min_search = sorted(search)[0]
#     for category in product_categories.keys():
#         if len(product_categories[category]['searches']) == min_search:
#             return print(f'\n La categoría con menores búsquedas es {category}')
#         else:continue
# search_minsearch(busqueda_tot)

# def search_maxsearch(search):
#     max_search = sorted(search, reverse=True)[0]
#     for category in product_categories.keys():
#         if len(product_categories[category]['searches']) == max_search:
#             return print(f'\n La categoría con mayores búsquedas es {category}')
#         else:continue

# search_maxsearch(busqueda_tot)



