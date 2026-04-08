from src.product import Product
from src.product_manager import ProductManager

def main():
    manager = ProductManager()

    print("=== BYSCOM Product Manager CLI ===")
    print("1. Thêm sản phẩm mới")
    print("2. Xem tất cả sản phẩm")
    print("3. Tìm theo category")
    print("4. Lọc theo giá")
    print("5. Tính tổng giá trị kho")
    print("6. Thoát")

    while True:
        choice = input("\nChọn chức năng (1-6): ").strip()

        if choice == "1":
            pid = int(input("ID: "))
            name = input("Tên sản phẩm: ")
            price = float(input("Giá (VND): "))
            category = input("Category: ")
            stock = int(input("Stock: "))

            product = Product(id=pid, name=name, price=price, category=category, stock=stock)
            manager.add_product(product)
            print("✅ Thêm thành công!")

        elif choice == "2":
            for p in manager.get_all_products():
                print(p)

        elif choice == "3":
            cat = input("Nhập category: ")
            results = manager.find_by_category(cat)
            for p in results:
                print(p)

        elif choice == "4":
            min_p = float(input("Giá tối thiểu: ") or 0)
            max_p = float(input("Giá tối đa: ") or float('inf'))
            results = manager.filter_by_price(min_p, max_p)
            for p in results:
                print(p)

        elif choice == "5":
            total = manager.get_total_value()
            print(f"💰 Tổng giá trị kho: {total:,.0f} VND")

        elif choice == "6":
            print("👋 Tạm biệt! Dữ liệu đã được lưu.")
            break

if __name__ == "__main__":
    main()
