# Ngày 5: pandas cơ bản cho CSV/JSON
# Mục tiêu: Làm quen pandas – sẽ dùng rất nhiều ở Phase 5 (Data Pipeline).

import json

import pandas as pd

df = pd.read_csv("Phase 1/Week 2/data/products.csv")
# # # them cot quantity
# # df['quantity'] = 0
# # # Tạo bảng quy tắc
# # mapping = {
# #     'Electronics': 10,
# #     'Clothing': 20,
# #     'Books': 30
# # }
# # df['quantity'] = df['category'].map(mapping).fillna(0)

# df['total']= df['price'] * df['quantity']

# df.to_csv("Phase 1/Week 2/data/products.csv", index=False)

# df_filtered = df[(df['price'] > 100) & (df['category'] == 'Electronics')]
# df_filtered.to_csv("Phase 1/Week 2/data/filtered_products.csv", index=False)
# df_filtered.to_json("Phase 1/Week 2/data/filtered_products.json", orient='records', lines=True)


with open("Phase 1/Week 2/data/product_shoppe.json", "r") as f:
    product_data = json.load(f)
    items = product_data[0]["items"]
    total = sum(item["price"] for item in items)

print(f"Total price: {total}")

