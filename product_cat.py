from lifestore_file import lifestore_sales, lifestore_products, lifestore_searches
#Productos por categorías
product_categories= {}

for element in lifestore_products:
    category = element[3]
    product = element[1]
    if category not in product_categories.keys():
        product_categories[category] = []
    else:
        product_categories[category].append(product)
    
for key in product_categories.keys():
    print(f'\n {key}:')
    for product in product_categories[key]:
        print(f'\t {product}')
    