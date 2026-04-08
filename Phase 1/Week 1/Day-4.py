# print("--------------------------------")
# print("Viết hàm nhận 2 tham số và trả về tổng của chúng")


# def Tong(a, b):
#     return a+b


# print("--------------------------------")
# print("Viết hàm nhận nhiều tham số và trả về tổng của chúng")


# def Tong_arg(*arg):
#     total = 0
#     for num in arg:
#         total += num
#     return total


# print(Tong_arg(1, 2, 3, 4, 5))

# print("--------------------------------")
# print("Viết hàm nhận **kwargs và in ra “Tên: … Tuổi: …”")


# def print_info(**kwargs):
#     name = kwargs.get("name", "Unknown")
#     age = kwargs.get("age", "Unknown")
#     print(f"Tên: {name}, Tuổi: {age}")


# print_info(name="Alice", age=30)

# print("--------------------------------")
# print("Viết hàm lambda tính bình phương một số")


# def dinhPhuong(x): return x ** 2


# print(dinhPhuong(5))

print("--------------------------------")

list_numbers = [1, 2, 3, 4, 5]
print("Sử dụng hàm map để tính bình phương của các số trong list")
squares = map(lambda x: x ** 2, list_numbers)
squares2 = [number ** 2 for number in list_numbers]
print(f"List bình phương của {list_numbers} là: {squares}")


# print("--------------------------------")
# print("Viết hàm calculate_total(items) sử dụng reduce để tính tổng giá của các item trong list")


# def calculate_total(items):
#     total = 0
#     for item in items:
#         total += item.get("price", 0)
#     return total


# list_dict = [{"name": "item1", "price": 10}, {
#     "name": "item2", "price": 20}, {"name": "item3", "price": 30}]
# total_price = calculate_total(list_dict)
# print(f"Tổng giá của các item là: {total_price}")
