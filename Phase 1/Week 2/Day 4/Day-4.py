# pathlib – Cách hiện đại
# Mục tiêu: Thay os.path bằng pathlib
import datetime
from pathlib import Path

import pandas as pd

# ## Viết script liệt kê tất cả file trong thư mục data/ bằng Path
# data_dir = Path("Phase 1/Week 2/data")
# # Kiểm tra xem thư mục có tồn tại không trước khi duyệt
# if data_dir.exists() and data_dir.is_dir():
#     for file in data_dir.iterdir():
#         print(file.name)
# else:
#     print("Thư mục 'data' không tồn tại!")

# ##Kiểm tra file tồn tại, tạo thư mục mới nếu chưa có (Path.mkdir)
# data_dir = Path("Phase 1/Week 2/new_folder")
# if(not data_dir.exists()):
#     data_dir.mkdir(parents=True)  # Tạo thư mục nếu chưa tồn tại
#     print("Thư mục 'new_folder' đã được tạo!")
# else:
#     print("Thư mục 'new_folder' đã tồn tại!")

# data_dir = Path("Phase 1/Week 2/data")
# file_path = data_dir / "products.csv"
# file_path_new= data_dir / "backup_products.csv"

# content = file_path.read_bytes()  # Đọc nội dung file
# file_path_new.write_bytes(content)  # Ghi nội dung vào file mới
# print(file_path_new)

##Viết hàm get_data_path(filename) trả về Path object đúng hệ điều hành.
# def get_data_path(filename):
#     data_dir = Path("Phase 1/Week 2/data")
#     return data_dir / filename

# print(get_data_path("products.csv"))

def backup_folder(folder_path):
    folder = Path(folder_path)
    if folder.exists() and folder.is_dir():
        backup_folder = folder.parent / "backup" / f"{datetime.date.today()}"
        backup_folder.mkdir(parents=True)
        for file in folder.iterdir():
            if file.is_file():
                backup_file = Path(backup_folder) / file.name
                backup_file.write_bytes(file.read_bytes())

backup_folder("Phase 1/Week 2/data")
