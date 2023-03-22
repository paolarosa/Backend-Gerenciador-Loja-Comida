from menu import products

def calculate_tab(orders):
    sum_orders = 0
    for element_order in orders:
        order_id = element_order["_id"]
        amount = element_order["amount"] 
        print(amount)
        for element_product in products:
            product_id = element_product["_id"]
            print(product_id)
            if product_id == order_id:
                sum_orders += element_product["price"] * amount

    return {"subtotal": f"${round(sum_orders, 2)}"}