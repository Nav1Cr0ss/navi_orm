


class CharField():

    def __init__(self, f_name: str, f_max: int, f_null: bool = False):
        self.f_name = f_name
        self.f_max = f_max
        self.f_is_null = "NULL" if f_null else "NOT NULL"
        # Table
        # self.fields.append(f"{self.f_name} CHAR({self.f_max}) {self.f_is_null},\n")
    def __str__(self):
        return f"CHAR({self.f_max}) {self.f_is_null}"
    def make_field(self):
        return f"CHAR({self.f_max}) {self.f_is_null},\n"

class Table():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Table, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        self.name = self.__class__.__name__
        self.fields = []


    def _get_data(self):
        print(f"{self.name} - {self.fields}")
    # @staticmethod
    # def print_fields():
    #     pass
    # def charfield(**kwargs):
    #     Table.fields.append(CharField2(**kwargs).make_field())