from typing import List

import psycopg2
from psycopg2 import Error
from psycopg2.extras import DictCursor
from navi_orm import orm
from settings import DB_URL, MODEL_MODULES

# import all models modules
modules_list = []
for i in MODEL_MODULES:
    modules_list.append(__import__(i))


class ModelService():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ModelService, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.model_classess = []
        self.class_attr_dict = {}
        self.query_strings = []
        self.is_table_created = False
        for module in modules_list:
            for mod in dir(module):
                try:
                    if issubclass(getattr(module, mod), orm.Table):
                        self.model_classess.append(getattr(module, mod))
                except TypeError:
                    pass
        for model_class in self.model_classess:
            attr_list = [attr for attr in dir(model_class) if not attr.startswith('_')]
            self.class_attr_dict[model_class.__name__] = [f'{attr} {str(getattr(model_class, attr))}'
                                                          for attr in attr_list]

    def create_table_in_db(self):
        print(self.query_strings)
        with psycopg2.connect(DB_URL) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                for string in self.query_strings:
                    cursor.execute(string)
                conn.commit()
        # if not self.is_table_created:

            # self.is_table_created = True

        # raise ValueError("таблицы уже созданы")

    def make_fields(self, fields: List[str]):
        fields_list = ""
        for field in fields[:-1]:
            fields_list += f'{field}'
        return fields_list

    def make_table_string(self):

        self.query_strings.append(''.join([f'CREATE TABLE IF NOT EXISTS  {k}  ({self.make_fields(v)});\n' for (k, v) in self.class_attr_dict.items()]))

    # def select_all_table_data(self):
    #     query_string = f"""SELECT * FROM {self.__name__}"""
    #     print(query_string)



if __name__ == "__main__":
    initial = ModelService()
    initial.make_table_string()
    initial.create_table_in_db()

