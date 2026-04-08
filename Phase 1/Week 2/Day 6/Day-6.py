import json
import logging
from datetime import datetime
from json.tool import main
from pathlib import Path

import pandas as pd

# Viết chương trình “Product Data Importer”:
# Đọc file CSV hoặc JSON (tự detect loại file)
# Làm sạch dữ liệu (loại bỏ trùng id, giá âm → đặt = 0)
# Thêm cột last_updated = datetime.now()
# Export ra cả 3 định dạng: CSV, JSON, Excel
# Ghi log mọi bước vào import.log

def lay_loai_file(duong_dan):
    """Trả về 'csv' hoặc 'json' dựa vào phần đuôi của file"""
    # os.path.splitext tách tên file thành (tên, đuôi)
    phan_duoi = Path(duong_dan).suffix.lower()  # Lấy phần đuôi và chuyển về chữ thường

    if phan_duoi == '.csv':
        return 'csv'
    elif phan_duoi == '.json':
        return 'json'
    else:
        raise ValueError("❌ Chỉ hỗ trợ file .csv hoặc .json!")

def doc_file_json(duong_dan):
    """Đọc file JSON - hỗ trợ cả dạng đơn giản và dạng thực tế từ web/API"""
    logging.info(f"Đang đọc file JSON: {duong_dan}")

    with open(duong_dan, 'r', encoding='utf-8') as file:
        du_lieu = json.load(file)        # Đọc toàn bộ nội dung JSON

    # Trường hợp 1: JSON là mảng trực tiếp []
    if isinstance(du_lieu, list):
        df = pd.DataFrame(du_lieu)
        logging.info("✅ JSON dạng mảng trực tiếp")
        return df

    # Trường hợp 2: JSON có wrapper {"data": [...], "success": true, ...}
    elif isinstance(du_lieu, dict):
        cac_key_co_the = ['data', 'products', 'items', 'result', 'payload']

        for key in cac_key_co_the:
            if key in du_lieu and isinstance(du_lieu[key], list):
                df = pd.DataFrame(du_lieu[key])
                logging.info(f"✅ Tìm thấy danh sách sản phẩm trong key '{key}'")
                return df

        # Nếu không tìm thấy key nào, coi như chỉ có 1 dòng
        df = pd.DataFrame([du_lieu])
        logging.warning("⚠️ Không tìm thấy mảng, chuyển thành 1 dòng dữ liệu")
        return df

    else:
        raise ValueError("❌ File JSON không đúng định dạng!")

def doc_file_csv(duong_dan):
    """Đọc file CSV đơn giản"""
    logging.info(f"Đang đọc file CSV: {duong_dan}")
    df = pd.read_csv(duong_dan)
    return df

def doc_file(duong_dan):
    loai_file = lay_loai_file(duong_dan)

    if loai_file == 'csv':
        return doc_file_csv(duong_dan)
    else:
        return doc_file_json(duong_dan)

def xoa_trung_id(df):
    """Xóa các dòng có id giống nhau, giữ lại dòng đầu tiên"""
    if 'id' not in df.columns:
        logging.warning("Cột 'id' không tồn tại, bỏ qua bước xóa trùng")
        return df

    so_dong_cu = len(df)
    df = df.drop_duplicates(subset=['id'], keep='first')
    so_dong_moi = len(df)

    logging.info(f"✅ Xóa trùng id: {so_dong_cu - so_dong_moi} dòng bị loại")
    return df

def sua_gia_am(df):
    """Nếu giá < 0 thì đổi thành 0"""
    if 'price' not in df.columns:
        logging.warning("Cột 'price' không tồn tại, bỏ qua bước sửa giá")
        return df

    so_gia_am = (df['price'] < 0).sum()          # Đếm số giá âm
    df['price'] = df['price'].clip(lower=0)      # Đổi tất cả giá âm thành 0

    logging.info(f"✅ Sửa giá âm: {so_gia_am} giá trị được đặt về 0")
    return df

def them_cot_last_updated(df):
    df['last_updated'] = datetime.now() # type: ignore
    logging.info("✅ Thêm cột 'last_updated' với giá trị hiện tại")
    return df

def lam_sach_du_lieu(df):
    """Hàm tổng hợp tất cả bước làm sạch"""
    logging.info("Bắt đầu làm sạch dữ liệu...")

    df = xoa_trung_id(df)
    df = sua_gia_am(df)
    df = them_cot_last_updated(df)

    return df

def xuat_file(df, ten_file_co_so="products_cleaned"):
    """Xuất ra 3 file: CSV, JSON, Excel"""
    # 1. Xuất CSV
    ten_csv = f"{ten_file_co_so}.csv"
    df.to_csv(ten_csv, index=False, encoding='utf-8')
    logging.info(f"✅ Đã xuất CSV: {ten_csv}")

    # 2. Xuất JSON
    ten_json = f"{ten_file_co_so}.json"
    df.to_json(ten_json, orient='records', force_ascii=False, indent=2)
    logging.info(f"✅ Đã xuất JSON: {ten_json}")

    # 3. Xuất Excel
    ten_excel = f"{ten_file_co_so}.xlsx"
    df.to_excel(ten_excel, index=False, engine='openpyxl')
    logging.info(f"✅ Đã xuất Excel: {ten_excel}")

    print("\n🎉 HOÀN THÀNH XUẤT FILE!")

def main():
    """Hàm chính - chạy toàn bộ chương trình"""

    print("🚀 PRODUCT DATA IMPORTER ")
    print("=" * 55)

    # Bước 1: Nhập đường dẫn file
    duong_dan = input("\nNhập đường dẫn file CSV hoặc JSON: ").strip()

    try:
        # Bước 2: Đọc file
        print("📥 Đang đọc file...")
        df = doc_file(duong_dan)
        print(f"✅ Đã đọc {len(df)} dòng dữ liệu")

        # Bước 3: Làm sạch dữ liệu
        print("🧹 Đang làm sạch dữ liệu...")
        df_sach = lam_sach_du_lieu(df)

        # Bước 4: Xuất file
        print("📤 Đang xuất 3 định dạng file...")
        xuat_file(df_sach)

        print("\n✅ CHƯƠNG TRÌNH HOÀN TẤT!")
        print("   Kiểm tra file import.log để xem chi tiết từng bước.")

    except Exception as loi:
        print(f"❌ Có lỗi xảy ra: {loi}")
        logging.error(f"Lỗi nghiêm trọng: {loi}")

if __name__ == "__main__":
    main()
    main()
