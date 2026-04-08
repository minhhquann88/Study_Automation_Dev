# list_products = [
#     {"name": "Product A", "price": 10, "quantity": 2},
#     {"name": "Product B", "price": 20, "quantity": 3},
#     {"name": "Product C", "price": 30, "quantity": 1}
# ]


# def In(products):
#     for product in products:
#         print(
#             f"Tên: {product['name']}, Giá: {product['price']}, Số lượng: {product['quantity']}")
#     print("--------------------------------")


# def calculate_total(items):
#     total = 0
#     for item in items:
#         total += item.get("price", 0) * item.get("quantity", 0)
#     return total


# print(f"Tổng giá của các sản phẩm là: {calculate_total(list_products)}")


# def add_product(products, name, price, quantity):
#     products.append({"name": name, "price": price, "quantity": quantity})
#     return products


# In(add_product(list_products, "Product D", 40, 5))


# def remove_product(products, name):
#     products[:] = [product for product in products if product["name"] != name]


# remove_product(list_products, "Product B")
# In(list_products)

# product = list(filter(lambda p: p["name"] == "Product A", list_products))
# print(product)

from functools import reduce


list_products=[
    {"name": "Product A", "price": 10, "quantity": 2},
    {"name": "Product B", "price": 20, "quantity": 3},
    {"name": "Product C", "price": 30, "quantity": 1}
]

def process_data(data:list[dict]) ->list:
    # return [item for item in data if item["price"] > 15]
    return list(filter(lambda item: item["price"] > 15, data))

filtered_products = process_data(list_products)
print(filtered_products)

avenger_price = reduce(lambda acc, item: acc + item["price"], list_products, 0)
print(f"Trung bình giá của các sản phẩm là: {avenger_price / len(list_products)}")



