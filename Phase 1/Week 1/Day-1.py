from typing import Any


name = "John"
age = 20
price = 10.5
is_student = True

print(type(name))
print(type(age))
print(type(price))
print(type(is_student))

print("--------------------------------")
prompt="nhap a:"
a = int(input(prompt))
prompt="nhap b:"
b = int(input(prompt))
print("tong cua a va b la:", a + b)
print("hieu cua a va b la:", a - b)
print("tich cua a va b la:", a * b)
print("thuong cua a va b la:", a / b)

print("--------------------------------")

prompt = "kiem tra chan/le:"
number = int(input(prompt))
print(f"{number} la so chan" if number % 2 == 0 else f"{number} la so le")

print("--------------------------------")

list_numbers = [1, 2, 3, 4, 5,12,5,3,6,2,76,8,100]
list_numbers.sort();
print("so lon nhat la:", list_numbers[-1])
print("so nho nhat la:", list_numbers[0])

print("--------------------------------")
student = {"name": "John", "age": 20, "score": [10, 20, 30, 40, 50]}
print(type(student))    
print(f"diem trung binh la: {sum(student['score'])/len(student['score'])}")
