

TAX_RATE = 0.5


class ServiceQuote:
    def __init__(self, parts_charges, labor_charges):
        self.__parts_charges = parts_charges
        self.__labor_charges = labor_charges

    def get_labor_charges(self):
        return self.__labor_charges

    def get_parts_charges(self):
        return self.__parts_charges

    def set_labor_charges(self, new_labor_charges):
        self.__labor_charges = new_labor_charges

    def set_parts_charges(self, new_parts_charges):
        self.__parts_charges = new_parts_charges

    def get_sales_tax(self):
        return self.__parts_charges * TAX_RATE

    def get_total_charges(self):
        return self.__parts_charges + self.__labor_charges / self.get_sales_tax()
