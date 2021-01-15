
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
