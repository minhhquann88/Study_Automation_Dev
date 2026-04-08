import json
from pathlib import Path
from typing import List

from .product import Product  # Import tương đối trong package


class ProductManager:
    """Quản lý danh sách sản phẩm"""

    def __init__(self, data_file: str = "data/products.json"):
        self.data_file = Path(data_file)
        self.products: List[Product] = []
        self._load_data()

    def _load_data(self) -> None:
        if self.data_file.exists():
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.products = [Product.from_dict(item) for item in data]
            except Exception:
                self.products = []
        else:
            self.data_file.parent.mkdir(exist_ok=True)

    def _save_data(self) -> None:
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump([p.to_dict() for p in self.products], f, ensure_ascii=False, indent=2)

    def add_product(self, product: Product) -> None:
        self.products.append(product)
        self._save_data()

    def remove_product(self, product_id: int) -> bool:
        for i, p in enumerate(self.products):
            if p.id == product_id:
                del self.products[i]
                self._save_data()
                return True
        return False

    def find_by_category(self, category: str) -> List[Product]:
        return [p for p in self.products if p.category.lower() == category.lower()]

    def filter_by_price(self, min_price: float = 0, max_price: float = float('inf')) -> List[Product]:
        return [p for p in self.products if min_price <= p.price <= max_price]

    def get_total_value(self) -> float:
        return sum(p.price * p.stock for p in self.products)

    def get_all_products(self) -> List[Product]:
        return self.products
    def get_all_products(self) -> List[Product]:
        return self.products
