#Ngày 1: File TXT cơ bản
#Mục tiêu: Đọc/ghi file text thuần túy

# Cách ĐÚNG (luôn dùng with)
# with open('Phase 1/Week 2/hello.txt', 'w', encoding='utf-8') as f:
#     f.write("Bot started at 2026-04-07\n") # ghi đè
# with open('Phase 1/Week 2/hello.txt', 'a', encoding='utf-8') as f:   # append
#     f.write("Crawling Shopee...\n") # ghi thêm vào cuối file
# with open('Phase 1/Week 2/Day-1/hello.txt', 'r', encoding='utf-8') as f:
#     content = f.read()           # toàn bộ file
#     lines = f.readlines()        # list các dòng

## Tạo file hello.txt và ghi câu “Xin chào BYSCOM Automation Team!” vào file.
# with open('Phase 1/Week 2/hello1.txt', 'w', encoding='utf-8') as f:
#     f.write("Xin chào BYSCOM Automation Team!\n")
# print("File đã được ghi thành công!")
# print("----------------------------------")

## Đọc toàn bộ nội dung file hello.txt và in ra màn hình.
# with open('Phase 1/Week 2/hello.txt', 'r', encoding='utf-8') as f:
#     content = f.read()
#     print(f"Nội dung của file hello.txt: {content}\n")

##Ghi thêm 5 dòng log (ví dụ: “Log 1: Bot started”, “Log 2: Crawling…”).
# with open('Phase 1/Week 2/hello.txt', 'a', encoding='utf-8') as f:
#     f.write('Log 1: Bot started\n')
#     f.write('Log 2: Crawling Shopee...\n')
#     f.write('Log 3: Bot stopped\n')
#     f.write('Log 4: Bot restarted\n')
#     f.write('Log 5: Bot stopped again\n')
# print("Các log đã được ghi vào file hello.txt thành công!")

# ## Đọc file theo dòng (readlines()) và in từng dòng có số thứ tự.
# with open('Phase 1/Week 2/hello.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     print("Các dòng trong file hello.txt:")
#     for i in range(len(lines)):
#         print(f"Dòng {i+1}: {lines[i].strip()}")

##Viết hàm write_log(message) ghi thời gian + message vào file app.log.
# from datetime import date

# def write_log(message):
#     with open('Phase 1/Week 2/app.log', 'a', encoding='utf-8') as f:
#         f.write(f"{date.today()}: {message}\n")

# write_log("Bot started")
# write_log("Crawling Shopee...")
# write_log("Error: Connection timeout")
# write_log("Error: Invalid response from server")

##
from functools import reduce


with open('Phase 1/Week 2/app.log', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    count = reduce(lambda acc, line: acc + (1 if "Error" in line else 0), lines, 0)
    print(f"Số dòng chứa 'Error' trong file app.log: {count}")