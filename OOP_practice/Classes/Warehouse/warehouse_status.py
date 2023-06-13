class Warehouse:
    def __init__(self, cash: int, is_empty: bool, items_value, all_items_cash):
        self.__cash = cash
        self.__is_empty = is_empty
        self.__items_value = items_value
        self.__all_items_cash = all_items_cash

    def get_cash(self):
        return self.__cash
