
class Field:
    def __init__(self, column_type, primary_key, **kwargs):
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = None

        if kwargs:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)


class CharField(Field):
    def __init__(self, max_length=100, primary_key=False, **kwargs):
        super().__init__(f'varchar({max_length})', primary_key, **kwargs)


class IntegerField(Field):
    def __init__(self, primary_key=False, **kwargs):
        super().__init__('bigint', primary_key, **kwargs)


class BooleanField(Field):
    def __init__(self, **kwargs):
        super().__init__('boolean', False, **kwargs)


class FloatField(Field):
    def __init__(self, primary_key=False, **kwargs):
        super().__init__('real', primary_key, **kwargs)


class TextField(Field):
    def __init__(self, primary_key=False, **kwargs):
        super().__init__('text', False, **kwargs)


class MetaModel(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        primaryKey = None
        fields = []
        mappings = dict()
        for k_col, v_col in attrs.items():
            if isinstance(v_col, Field):
                mappings[k_col] = v_col

                if v_col.primary_key:
                    if primaryKey:
                        raise Exception(f'Duplicat primary key for field: {k_col}')

                    primaryKey = k_col
                else:
                    fields.append(k_col)

        if primaryKey is None:
            primaryKey = 'id'

        for k_col in mappings:
            attrs.pop(k_col)

        attrs['__mappings__'] = mappings
        attrs['__table__'] = table_name = attrs.get('Meta').db_table or name
        attrs['__pimary_key__'] = primaryKey
        attrs['__field__'] = fields

        attrs['__insert__'] = f"INSERT INTO {table_name}({','.join(mappings.keys())}) VALUES({cls.create_args_positions(len(mappings))})"
        attrs['__delete__'] = f"DELETE FROM {table_name} WHERE {primaryKey} = ?"
        attrs['__update__'] = f"UPDATE {table_name} SET {','.join(map(lambda x: f'{x} = ?', fields))} WHERE {primaryKey} = ?"
        attrs['__select__'] = f"SELECT {primaryKey}, {','.join(fields)} FROM {table_name}"

        return type.__new__(cls, name, bases, attrs)

    @staticmethod
    def create_args_positions(args_num):
        return ','.join('?' for _ in range(args_num))


class Model(dict, metaclass=MetaModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"'Model' object has no attribute '{key}'")

    def save(self):
        field = []
        values = []
        for k, v in self.__mappings__.items():
            field.append(k)
            values.append(getattr(self, k, v.default))

        values_temp = tuple(f"'{x}'" if isinstance(x, str) else str(x) for x in values)
        print(self.__insert__.replace('?', '%s') % values_temp)

    def delete(self):
        pass

    def update(self):
        pass

    @classmethod
    def find(cls):
        pass


class User(Model):

    id = IntegerField()
    name = CharField(max_length=20, default='cc')
    email = CharField(max_length=20)
    password = CharField(max_length=20)

    class Meta:
        db_table = 'users'


if __name__ == '__main__':
    u = User(id=1, name='cs', email='cs@126.com', password='pwd')
    u.save()
