# JSON cơ bản & Nested JSON
# Mục tiêu: Xử lý JSON – định dạng #1 khi crawl TikTok/Shopee API.

##
import json
import os

dict_product = {
    "name": "Laptop Dell XPS 13",
    "price": 999.99,
    "quantity": 10
}
# Tạo dictionary sản phẩm → chuyển thành JSON và ghi file product.json.
# with open("Phase 1/Week 2/Day 3/product.json", "w", encoding="utf-8") as file:
#     json.dump(dict_product, file, ensure_ascii=False, indent=4)

# Đọc file JSON và chuyển về dictionary (json.load)
# with open("Phase 1/Week 2/Day 3/product.json", "r", encoding="utf-8") as file:
#     product_data = dict(json.load(file))
# print(product_data)

dict_product_shoppe = {
    "items": [
        {
            "id": 1,
            "name": "Tai nghe Bluetooth Sony",
            "price": 2500000,
            "shop": {"name": "Sony Official Store", "city": "Hà Nội"}
        },
        {
            "id": 2,
            "name": "Loa Marshall Emberton",
            "price": 3800000,
            "shop": {"name": "Marshall Vietnam", "city": "TP.HCM"}
        }
    ]
}

# with open("Phase 1/Week 2/Day 3/product_shoppe.json", "w", encoding="utf-8") as file:
#     json.dump(dict_product_shoppe, file, ensure_ascii=False, indent=3)

json_data = {
    "items": [
        {
            "id": 1,
            "name": "Tai nghe Bluetooth Sony",
            "price": 2500000,
            "shop": {"name": "Sony Official Store", "city": "Hà Nội"}
        },
        {
            "id": 2,
            "name": "Loa Marshall Emberton",
            "price": 3800000,
            "shop": {"name": "Marshall Vietnam", "city": "TP.HCM"}
        }
    ]
}


# def extract_product_name(json_data):

#     product_names = [item["name"] for item in json_data.get("items", [])]
#     return product_names


# print(extract_product_name(json_data))

new_product = {
    "id": 3,
    "name": "Bàn phím cơ Keychron K2",
    "price": 3200000,
    "shop": {"name": "Keychron Vietnam", "city": "Hà Nội"}}

# with open("Phase 1/Week 2/Day 3/product_shoppe.json", "r", encoding="utf-8") as file:
#     data = json.load(file)
#     data["items"].append(new_product)

# with open("Phase 1/Week 2/Day 3/product_shoppe.json", "w", encoding="utf-8") as file:
#     json.dump(data, file, ensure_ascii=False, indent=3)


# Xử lý lỗi khi đọc/ghi file JSON
# file_path = "data.json"

# # 1. Kiểm tra tồn tại/trống để chủ động tạo mới
# if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
#     with open(file_path, "w", encoding="utf-8") as f:
#         json.dump({"items": []}, f)

# # 2. Sau đó mới đọc và dùng try...except để phòng hờ file bị hỏng cấu trúc
# try:
#     with open(file_path, "r", encoding="utf-8") as f:
#         data = json.load(f)
# except json.JSONDecodeError:
#     print("⚠️ File bị lỗi cấu trúc! Đang dùng dữ liệu trống.")
#     data = {"items": []}

with open("Phase 1/Week 2/Day 3/product_shoppe.json", "r", encoding="utf-8") as file:
    df = json.load(file)
print(df["items"][:5])
total = sum(item.get("price", 0) for item in df["items"])

# them truong total_price vao root
df["total_price"] = total
with open("Phase 1/Week 2/Day 3/product_shoppe.json", "w", encoding="utf-8") as file:
    json.dump(df, file, ensure_ascii=False, indent=3)
