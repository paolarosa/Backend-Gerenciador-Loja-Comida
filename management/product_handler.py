from menu import products

def get_product_by_id(id):
    if not type(id) == int:
        raise TypeError("product id must be an int")
    for element in products:
        if id == element["_id"]:
            return element
    return {}
        

def get_products_by_type(type_product):
    if not type(type_product) == str:
        raise TypeError("product type must be a str")
    new_list = []
    for element in products:
        if type_product == element["type"]:
            new_list.append(element)
    return new_list


def add_product(menu: list, **kwargs: dict):
    id = 0
    for el in range(0, len(menu)):
        if menu[el]["_id"] > id:
            id = menu[el]["_id"]
    kwargs.update({"_id": id + 1})
    menu.append(kwargs)
    return kwargs
        

def menu_report():
    product_count = len(products)
    sum_products = 0
    type_product = {}

    for element in products:
        sum_products += element["price"]
        types_count = get_products_by_type(element["type"])
        type_product.update({element["type"]:len(types_count)})

    common_type = 0
    type_key = ""
    for chave, valor in type_product.items():
        if valor > common_type:
            common_type = valor
            type_key = chave
            
    average_price = round(sum_products/product_count, 2)

    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {type_key}"
  
