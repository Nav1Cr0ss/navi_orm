import psycopg2

from settings import DB_URL


class CharField():

    def __init__(self, f_name: str, f_max: int, f_null: bool = False):
        self.f_name = f_name
        self.f_max = f_max
        self.f_is_null = "NULL" if f_null else "NOT NULL"

    def __str__(self):
        return f"CHAR({self.f_max}) {self.f_is_null}"


class Table():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Table, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.name = self.__class__.__name__
        self.fields = []
    @classmethod
    def _select_all_table_data(self):
        query_string = f"""SELECT * FROM {self.__name__}"""

        with psycopg2.connect(DB_URL) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query_string)
                result = cursor.fetchall()
        return result

    def _get_data(self):
        print(f"{self.name} - {self.fields}")




