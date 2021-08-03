from navi_orm import orm, main


class TableName22(orm.Table):
    first_name = orm.CharField(f_name='first', f_max=250, f_null=True)
    second_name = orm.CharField(f_name='second', f_max=250, f_null=True)

class TableName12(orm.Table):
    first_name = orm.CharField(f_name='first', f_max=250, f_null=True)
    second_name = orm.CharField(f_name='second', f_max=250, f_null=True)

if __name__ == "__main__":
   for row in  TableName12._select_all_table_data():
       print(row[0])

