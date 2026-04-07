# Ngày 5: Exception Handling (try-except)
# Mục tiêu: Code không bị crash khi người dùng nhập sai – rất quan trọng khi chạy bot thực tế.


# print("--------------------------------")
# a = int(input("Nhập một số nguyên a: "))
# b = int(input("Nhập một số nguyên b: "))
# while True:
#     try:
#         print(f"Kết quả của {a} chia cho {b} là: {a/b}")
#         break  # Thoát khỏi vòng lặp nếu không có lỗi
#     except ZeroDivisionError:
#         print("Lỗi: Không thể chia cho 0. Vui lòng nhập lại.")
#         b = int(input("Nhập một số nguyên b khác: "))

# print("--------------------------------")
# strA = input("Nhập một chuỗi strA: ")
# while True:
#     try:
#         x = int(strA)
#         print(f"Giá trị số nguyên của strA là: {x}")
#         break  # Thoát khỏi vòng lặp nếu không có lỗi
#     except ValueError:
#         print("Lỗi: strA không phải là một số nguyên. Vui lòng nhập lại.")
#         strA = input("Nhập một chuỗi strA khác: ")

# print("--------------------------------")
# print("Viết hàm mở file, nếu file không tồn tại thì in “File không tồn tại” (không crash)")


# def open_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
#             print(content)
#     except FileNotFoundError:
#         print("File không tồn tại.")


# open_file("Phase 1/Week 1/non_existent_file.txt")

print("--------------------------------")
print("Viết hàm nhận 2 số từ input, chia chúng, bắt tất cả lỗi có thể xảy ra.")
while True:
    try:
        a1 = int(input("Nhập một số nguyên a1: "))
        a2 = int(input("Nhập một số nguyên a2: "))
        print(f"Kết quả của {a1} chia cho {a2} là: {a1/a2}")
        break  # Thoát khỏi vòng lặp nếu không có lỗi
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0. Vui lòng nhập lại.")
    except ValueError:
        print("Lỗi: a1 hoặc a2 không phải là một số nguyên. Vui lòng nhập lại.")

print("--------------------------------")
print("Viết hàm safe_divide(a, b) trả về kết quả hoặc thông báo lỗi đẹp.")


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Lỗi: Không thể chia cho 0."
    except TypeError:
        return "Lỗi: Cả a và b phải là số."


print(safe_divide(10, 2))  # Kết quả: 5.0
print(safe_divide(10, 0))  # Kết quả: Lỗi: Không thể chia cho 0.
print(safe_divide("10", 2))  # Kết quả: Lỗi: Cả a và b phải là số.
