from Inventory import Inventory
from Book import Book

# 最近在同步学Java，所以写代码时我想尝试调用接口的方式，或者应该说代码风格弄成类似Java的那种，所以写的繁琐了一点。
# 下面的demo是AI帮忙弄的一个，
if __name__ == "__main__":
    b1 = Book("Python入门", 59.9, 10, categories="编程", author="张三")
    b2 = Book("算法", 79.0, 5, categories="编程", author="李四")
    b3 = Book("三体", 45.0, 3, categories="小说", author="刘慈欣")

    inventory1 = Inventory()
    inventory2 = Inventory()

    inventory1.add_Book(b1, 2)
    inventory1.add_Book(b2, 1)
    inventory2.add_Book(b3, 3)

    print("inventory1 总数:", inventory1.getTotalBookCount())
    print("inventory1 编程类目数:", inventory1.getTotalCategoriesCount())
    print("b1 在 inventory1 数量:", inventory1.find_Book(b1))
    print("b1 在 inventory1 编程 数量:", inventory1.find_BookInCategories(b1, "编程"))

    merged = Inventory.merge_Inventory(inventory1, inventory2)
    print("merged 总数:", merged.getTotalBookCount())

    Inventory.exchange_Inventory(inventory1, inventory2)
    print("交换后 inventory1 总数:", inventory1.getTotalBookCount())
    print("交换后 inventory2 总数:", inventory2.getTotalBookCount())

    print("库存实例数:", Inventory.getTotalInventoryCount())

    b4 = Book("Python入门", 59.9, 10, categories="编程", author="张三")
    b4.operation.editPrice(35.5)
    # 尽量屏蔽了内部工具函数，无法使用b4.set_Price() or 直接 b4.price = value...
