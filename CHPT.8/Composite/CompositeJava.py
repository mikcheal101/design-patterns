from abc import ABC


class IDepartment(ABC):
    def printDepartmentName(self):
        """ abstract class method """
        pass


class FinancialDepartment(IDepartment):
    def __init__(self, id: int, name: str) -> None:
        super().__init__()
        self.id = id
        self.name = name

    def printDepartmentName(self):
        print(self.name)


class SalesDepartment(IDepartment):
    def __init__(self, id: int, name: str) -> None:
        super().__init__()
        self.id = id
        self.name = name

    def printDepartmentName(self):
        print(self.name)


class HeadDepartment(IDepartment):
    def __init__(self, id: int, name: str) -> None:
        super().__init__()
        self.id = id
        self.name = name
        self.sub_departments = []

    def printDepartmentName(self):
        _ = [dept.printDepartmentName() for dept in self.sub_departments]

    def addDepartment(self, department: IDepartment):
        self.sub_departments.append(department)

    def removeDepartment(self, department: IDepartment):
        self.sub_departments.remove(department)


if __name__ == "__main__":
    sales = SalesDepartment(1, "Sales Department I")
    sales_two = SalesDepartment(2, "Sales Department II")
    finance = FinancialDepartment(3, "Finance Department I")
    finance_two = FinancialDepartment(4, "Finance Department II")

    subsidiary_one = HeadDepartment(5, "Subsidiary I")
    subsidiary_two = HeadDepartment(6, "Subsidiary II")

    group = HeadDepartment(7, "Holding")

    subsidiary_one.addDepartment(sales)
    subsidiary_one.addDepartment(finance)

    subsidiary_two.addDepartment(sales_two)
    subsidiary_two.addDepartment(finance_two)

    group.addDepartment(subsidiary_one)
    group.addDepartment(subsidiary_two)

    group.printDepartmentName()