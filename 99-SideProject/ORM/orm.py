
#  reference Django ORM


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

        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v

        for k in mappings:
            attrs.pop(k)

        attrs['__mappings__'] = mappings
        attrs['__table__'] = attrs.get('Meta').db_table or name
        return type.__new__(cls, name, bases, attrs)


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

    @staticmethod
    def join(params):
        return ','.join([f"'{x}'" if isinstance(x, str) else str(x) for x in params])

    def save(self):
        field = []
        values = []
        for k, v in self.__mappings__.items():
            field.append(k)
            values.append(getattr(self, k, v.default))

        print(f"SQL: INSERT INTO {self.__table__}({','.join(field)}) VALUES({self.join(values)})")

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
