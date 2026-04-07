from typing import Any


# name = "John"
# age = 20
# price = 10.5
# is_student = True

# print(type(name))
# print(type(age))
# print(type(price))
# print(type(is_student))

# print("--------------------------------")
# a = int(input("nhap a:"))
# b = int(input("nhap b:"))
# print(f"tong cua a va b la: {a + b}")
# print(f"hieu cua a va b la: {a - b}")
# print(f"tich cua a va b la: {a * b}")
# print(f"thuong cua a va b la: {a / b}")

# # print("--------------------------------")

# number = int(input("kiem tra chan/le:"))
# print(f"{number} la so chan" if number % 2 == 0 else f"{number} la so le")

# print("--------------------------------")

# list_numbers = [1, 2, 3, 4, 5,12,5,3,6,2,76,8,100]
# list_numbers.sort();
# print("so lon nhat la:", list_numbers[-1])
# print("so nho nhat la:", list_numbers[0])

# print("--------------------------------")
# student = {"name": "John", "age": 20, "score": [10, 20, 30, 40, 50]}
# print(type(student))    
# print(f"diem trung binh la: {sum(student['score'])/len(student['score'])}")

# print("--------------------------------")
# print("Chuyen list thanh set va nguoc lai")
# list_numbers2 = [1, 2, 3, 4, 5,12,5,3,6,2,76,8,100]
# set_numbers = set(list_numbers2) #chuyen list thanh set
# print(set_numbers)
# print(type(set_numbers))
# list_numbers3 = list(set_numbers)#chuyen set thanh list
# print(list_numbers3)
# print(type(list_numbers3))

# print("--------------------------------")
# print('chuoi doi xung')
# string = input("nhap chuoi:")
# if string == string[::-1]:
#     print("chuoi doi xung")
# else:
#     print("chuoi khong doi xung")

print("--------------------------------")
name = input("nhap ten san pham:")
age = int(input("nhap gia san pham:"))
quantity = int(input("nhap so luong san pham:"))
print(f"ten san pham: {name}, gia san pham: {age}, so luong san pham: {quantity}")
print(f"tong tien san pham: {age * quantity}$")