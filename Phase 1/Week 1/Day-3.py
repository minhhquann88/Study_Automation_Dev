print("Tạo list bình phương của các số từ 1 đến 20 (comprehension)")
list_numbers = list(range(1, 21))
squares = [number ** 2 for number in list_numbers]
print(f"List bình phương của các số từ 1 đến 20 là: {squares}")

print("--------------------------------")
print('Lọc ra các số chia hết cho 3 trong list 1–50')
list_numbers2 = list(range(1, 51))
div_by_3 = [number for number in list_numbers2 if number % 3 == 0]
print(f"Các số chia hết cho 3 trong list 1–50 là: {div_by_3}")

print("--------------------------------")
print("Tạo dict {1: 1, 2: 4, 3: 9, ..., 10: 100} (bình phương)")
dict = {number: number ** 2 for number in range(1, 11)}
print(f"Dict bình phương từ 1 đến 10 là: {dict}")

print("--------------------------------")
list_fruits = ["apple", "banana", "cherry", "date", "elderberry"]
dict_fruits = {fruit[0]: fruit for fruit in list_fruits}
print(f"Dict từ list fruits là: {dict_fruits}")

print("--------------------------------")
print("Tạo dict bình phương của các số chẵn từ 1 đến 20 (comprehension)")
list_numbers3 = list(range(1, 21))
dict_even_powers = {number: number **
                    2 for number in list_numbers3 if number % 2 == 0}
print(f"Dict bình phương của các số chẵn từ 1 đến 20 là: {dict_even_powers}")

print("--------------------------------")
list_strings = ["hello", "world", "python", "programming"]
list_filtered = [s for s in list_strings if len(s) > 5]
print(f"List các chuỗi có độ dài lớn hơn 5 là: {list_filtered}")
