# Tạo file products.csv với header: id,name,price,category và 10 dòng dữ liệu mẫu
# 1. Chuẩn bị dữ liệu mẫu (10 dòng)
import numpy as np
import pandas as pd
data = {
    'id': range(1, 11),
    'name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headset',
             'Webcam', 'Speaker', 'USB Drive', 'Hard Drive', 'Tablet'],
    'price': [1500, 25, 45, 200, 50, 60, 80, 15, 100, 300],
    'category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories',
                 'Electronics', 'Electronics', 'Accessories', 'Electronics', 'Electronics']
}
# CSV
# import csv
# with open('products.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.DictWriter(f, fieldnames=data.keys())
#     writer.writeheader()
#     for i in range(10):
#         writer.writerow({key: value[i] for key, value in data.items()})

# # PANDAS
# df = pd.DataFrame(data)
# df.to_csv('Phase 1/Week 2/products.csv', index=False, encoding='utf-8')

# Đọc file products.csv và in ra dưới dạng bảng đẹp.
# df = pd.read_csv('Phase 1/Week 2/products.csv')
# print(df.to_string(index=False))

# Thêm 1 sản phẩm mới vào file CSV mà không ghi đè toàn bộ file.
# df = pd.read_csv('Phase 1/Week 2/products.csv')
# new_product = pd.DataFrame({
#     'id': [11, 12],
#     'name': ['Smartphone', 'Tablet'],
#     'price': [800, 300],
#     'category': ['Electronics', 'Electronics']
# })
# df = pd.concat([df, new_product], ignore_index=True)
# df.to_csv('Phase 1/Week 2/products.csv', index=False, encoding='utf-8')

# # Lọc và ghi ra file mới cheap_products.csv chỉ những sản phẩm giá dưới 100.
# df = pd.read_csv('Phase 1/Week 2/products.csv')
# cheap_products = df[df['price'] < 100]
# cheap_products.to_csv('Phase 1/Week 2/cheap_products.csv',
#                       index=False, encoding='utf-8')

# Viết hàm export_to_csv(data: list[dict], filename: str)
# def export_to_csv(data: list[dict], filename: str):
#     df = pd.DataFrame(data)
#     df.to_csv(filename, index=False, encoding='utf-8')


# new_products = [
#     {'id': 13, 'name': 'Mouse Pad', 'price': 10, 'category': 'Accessories'},
#     {'id': 14, 'name': 'External SSD', 'price': 120, 'category': 'Electronics'}
# ]
# export_to_csv(new_products, 'Phase 1/Week 2/new_products.csv')

##
# Tạo dữ liệu mẫu cho 1000 dòng
# data = {
#     'ID': range(1, 1001),
#     'Product_Name': [f'Product_{i}' for i in range(1, 1001)],
#     # Giá ngẫu nhiên từ 50 - 500
#     'Price': np.random.randint(50, 500, size=1000),
#     # Tồn kho ngẫu nhiên từ 0 - 100
#     'Stock': np.random.randint(0, 100, size=1000),
#     'Category': np.random.choice(['Electronics', 'Home', 'Office', 'Sport'], size=1000)
# }

# # Tạo DataFrame
# df_large = pd.DataFrame(data)

# # Lưu thành file CSV
# df_large.to_csv('data_mau.csv', index=False)
# print("Đã tạo file data_mau.csv thành công!")

# tinh tong gia tri cua cot Price trong file data_mau.csv
# df = pd.read_csv('Phase 1/Week 2/data_mau.csv')
# print(df.head())
# total_price = df['Price'].sum()
# print(f"Tổng giá trị của cột Price là: {total_price}")
