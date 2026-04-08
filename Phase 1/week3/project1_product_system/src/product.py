from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Dict


@dataclass
class Product:
    """Class đại diện cho 1 sản phẩm"""
    id: int
    name: str
    price: float
    category: str
    stock: int = 0
    created_at: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> Dict:
        data = asdict(self)
        data['created_at'] = self.created_at.isoformat()
        return data

    @classmethod
    def from_dict(cls, data: Dict) -> 'Product':
        if 'created_at' in data:
            data['created_at'] = datetime.fromisoformat(data['created_at'])
        return cls(**data)

    def update_stock(self, quantity: int) -> None:
        self.stock += quantity

    def __str__(self) -> str:
        return f"[{self.id}] {self.name} | Giá: {self.price:,}đ | Kho: {self.stock}"

    def __repr__(self) -> str:
        return self.__str__()
