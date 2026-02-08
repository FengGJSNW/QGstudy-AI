from __future__ import annotations
from typing import Dict, List

from Book import Book

# 异常处理
class InventoryError(Exception):                pass
class InventoryLockedError(InventoryError):     pass
class BookNotFoundError(InventoryError):        pass
class InvalidCountError(InventoryError):        pass


class Inventory:
    Inventory_count = 0

    def __init__(self):
        self.Store: Dict[str, List[Book]] = {}          
        self.lock: bool = False                         # 操作锁，最近在学c++的多线程，学到类似的，所以加了个锁，后期尝试python的多线程编写玩玩

        Inventory.Inventory_count += 1

    def _check_lock(self):
        if self.lock:
            raise InventoryLockedError("当前库存已锁定/有进程正在操作，无法执行该操作")

    def _check_count(self, count: int):
        if not isinstance(count, int) or count <= 0:
            raise InvalidCountError("count 必须是正整数")

    def _get_category_of(self, book: Book, fallback: str = "未分类") -> str:
        cat = getattr(book, "categories", None)
        return cat if cat else fallback

    # 库与书的交互
    def add_Book(self, book: Book, count: int = 1):
        self._check_lock()
        self.lock = True
        self._check_count(count)

        cat = self._get_category_of(book)
        if cat not in self.Store:
            self.Store[cat] = []

        for _ in range(count):
            self.Store[cat].append(book)
        self.lock = False

    def remove_Book(self, book: Book, count: int = 1):
        self._check_lock()
        self.lock = True
        self._check_count(count)

        book_id = book.information.getId()

        removed = 0
        for cat, lst in list(self.Store.items()):
            i = len(lst) - 1
            while i >= 0 and removed < count:
                if lst[i].information.getId() == book_id:
                    lst.pop(i)
                    removed += 1
                i -= 1

            if len(lst) == 0:
                del self.Store[cat]

            if removed == count:
                self.lock = False
                return

        self.lock = False
        raise BookNotFoundError(f"库存中该书数量不足：需要移除 {count} 本，只移除了 {removed} 本")

    def find_Book(self, book: Book) -> int:
        book_id = book.information.getId()
        total = 0
        for lst in self.Store.values():
            total += sum(1 for b in lst if b.information.getId() == book_id)
        return total

    def find_BookInCategories(self, book: Book, categories: str) -> int:
        if categories not in self.Store:
            return 0

        book_id = book.information.getId()
        return sum(1 for b in self.Store[categories] if b.information.getId() == book_id)

    # 库与库的交互
    @staticmethod
    def exchange_Inventory(inventory_a: "Inventory", inventory_b: "Inventory"):
        if inventory_a.lock or inventory_b.lock:
            raise InventoryLockedError("当前库存已锁定/有进程正在操作，无法交换")
        inventory_a.lock = inventory_b.lock = True

        try:
            inventory_a.Store, inventory_b.Store = inventory_b.Store, inventory_a.Store
        finally:
            inventory_a.lock = inventory_b.lock = False


    @staticmethod
    def merge_Inventory(inventory_a: "Inventory", inventory_b: "Inventory") -> "Inventory":
        if inventory_a.lock or inventory_b.lock:
            raise InventoryLockedError("当前库存已锁定/有进程正在操作，无法合并")
        inventory_a.lock = inventory_b.lock = True

        merged = Inventory()

        for cat, lst in inventory_a.Store.items():
            merged.Store[cat] = list(lst)

        for cat, lst in inventory_b.Store.items():
            merged.Store.setdefault(cat, []).extend(lst)

        inventory_a.lock = inventory_b.lock = False
        return merged

    # 库自己的信息
    def getTotalBookCount(self) -> int:
        return sum(len(lst) for lst in self.Store.values())

    def getTotalCategoriesCount(self) -> int:
        return len(self.Store)

    @classmethod
    def getTotalInventoryCount(cls) -> int:
        return cls.Inventory_count


