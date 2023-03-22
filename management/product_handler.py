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


def add_product(menu: list, **kwargs: dict):
    id = 0
    for el in range(0, len(menu)):
        if menu[el]["_id"] > id:
            id = menu[el]["_id"]
    kwargs.update({"_id": id + 1})
    menu.append(kwargs)
    print(len(menu))
    return kwargs
        

"""     if len(menu) != 0:
        menu["_id"] = len(menu) + 1
    if len(menu) == 0:
        menu["_id"] = 1 """

