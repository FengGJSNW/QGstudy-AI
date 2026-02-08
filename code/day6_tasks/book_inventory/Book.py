from __future__ import annotations

class Book:
    auto_id = 0
    all_count = 0

    def __init__(self, name: str, price: float, count: int,
                 categories: str = "未分类",author: str = "未记录",):
        if not name:        raise ValueError("name不能为空")
        if price is None:   raise ValueError("price不能为空")
        if count is None:   raise ValueError("count不能为空")
        if price < 0:       raise ValueError("price不能为负")
        if count < 0:       raise ValueError("count不能为负")

        self.__name = name
        self.__price = price
        self.__count = count
        self.__categories = categories
        self.__author = author
        self.__id = Book.auto_id

        Book.auto_id += 1
        Book.all_count += count

        self.information = Book.Information(self)
        self.operation = Book.Operation(self)

    # 只读
    @property
    def id(self) -> int:            return self.__id
    @property
    def name(self) -> str:          return self.__name
    @property
    def categories(self) -> str:    return self.__categories
    @property
    def author(self) -> str:        return self.__author
    @property
    def price(self) -> float:       return self.__price
    @property
    def count(self) -> int:         return self.__count

    # 修改
    def __set_price(self, value: float):
        if value is None:
            raise ValueError("price不能为空")
        if value < 0:
            raise ValueError("price不能为负")
        self.__price = value

    def __set_name(self, value: str):
        if not value:
            raise ValueError("name不能为空")
        self.__name = value

    def __set_author(self, value: str):
        if value is None:
            raise ValueError("author不能为空")
        self.__author = value

    def __set_category(self, value: str):
        if value is None:
            raise ValueError("设置categories时不能为空")
        self.__categories = value

    def __add_stock(self, delta: int):
        if not isinstance(delta, int) or delta <= 0:
            raise ValueError("增加的数量必须为正整数")
        self.__count += delta
        Book.all_count += delta

    def __reduce_stock(self, delta: int):
        if not isinstance(delta, int) or delta <= 0:
            raise ValueError("减少的数量必须为正整数")
        if delta > self.__count:
            raise ValueError("库存不足")
        self.__count -= delta
        Book.all_count -= delta

    def __set_count_direct(self, new_count: int):
        if not isinstance(new_count, int):
            raise ValueError("count必须是整数")
        if new_count < 0:
            raise ValueError("count不能为负")

        old = self.__count
        self.__count = new_count
        Book.all_count += (new_count - old)

    # 信息访问接口
    class Information:
        def __init__(self, book: Book):
            self.__book = book

        def getId(self) -> int:
            return self.__book._Book__id

        def getName(self) -> str:
            return self.__book._Book__name

        def getPrice(self) -> float:
            return self.__book._Book__price

        def getAuthor(self) -> str:
            return self.__book._Book__author

        def getCategory(self) -> str:
            return self.__book._Book__categories

        def getCount(self) -> int:
            return self.__book._Book__count
        
    # 信息修改接口
    class Operation:
        def __init__(self, book : Book):
            self.__book = book

        def editName(self, value: str):
            self.__book._Book__set_name(value)

        def editPrice(self, value: float):
            self.__book._Book__set_price(value)

        def editAuthor(self, value: str):
            self.__book._Book__set_author(value)

        def editCategory(self, value: str):
            self.__book._Book__set_category(value)

        def editCount_direct(self, new_count: int):
            self.__book._Book__set_count_direct(new_count)

        def editCount_indirect(self, delta: int):
            if not isinstance(delta, int) or delta == 0:
                raise ValueError

            if delta > 0:
                self.__book._Book__add_stock(delta)
            else:
                self.__book._Book__reduce_stock(-delta)
