from menu import products

def get_product_by_id(id):
    for element in products:
        if id == element["_id"]:
            return element
    return {}
        
        
""" print(get_product_by_id(25))  """

def get_products_by_type(type):
    new_list = []
    for element in products:
        if type == element["type"]:
            new_list.append(element)
    return new_list
""" print(get_products_by_type("fruit")) """