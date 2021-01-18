
"""
利用ORM可实现什么功能？
举个例子，数据库中有一个User表，表中有两个字段id（主键）, name（名字），如何新增加一个数据？
利用ORM，使用者无需编写SQL代码，可基于类来实现，类似如下代码

1、首先定义一个User类
class User(Model):
    id = IntegerField(primary_key=True)
    name = StringField()

2、实例化类对象并初始化值
new_user = User(id='123456', name='LiMing')

3、调用方法保存
new_user.save()

使用者无需掌握SQL知识，即可完成数据库操作
"""

# 这里使用了异步mysql库
# 本文暂时不涉及具体的aiomysql知识
import aiomysql


# 用来定义数据库的数据类型（以MySQL数据库为例）
class Field():
    def __init__(self, name, column_type, primary_key, default):
        self.name = name      # 字段名
        self.column_type = column_type  # 字段类型
        self.primary_key = primary_key  # 该字段是否作为主键
        self.default = default          # 该字段的默认值

# 字符串类型，默认 varchar(100)
class StringField(Field):

    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)

# Bool类型, 无法作为主键，primary属性直接赋值False
class BooleanField(Field):

    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)

# 整数类型
class IntegerField(Field):

    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)

# 浮点类型
class FloatField(Field):

    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)

# 长文本类型
class TextField(Field):

    def __int__(self, name=None, default=None):
        super().__int__(name, 'text', False, default)

# 返回 ?,?,? 这样的形式，?的数量取决于参数num，用于在SQL语句模板中占位
# 如 insert into tableName values(?,?,?);
# 其中的?由该函数动态生成
def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ', '.join(L)

# 开始定义元类
# 目的：对于用户创建的类进行修改
class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):

        # 假定用户创建的类的父类是Model,不进行任何操作，因为需要修改的是用户自定义类
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        # 因为用户创建的类应当与一个数据库中的表挂钩，也就是关系映射
        # 用户对这个类的操作会影响数据库中对应表的操作，无需使用SQL语句直接与数据库打交道，方便使用
        # 因为这一切都交给ORM框架了，所以对于编写者来说，需要从用户定义的类中获取需要的信息，然后代替用户实现数据库的操作
        # 需要获取的数据有：表名，主键，其他字段，用户类中的映射关系

        # 尝试从类的__table__属性中获取表名，没找到就使用用户定义的类名作为表名
        tableName = attrs.get('__table__', None) or name

        # 稍后获取
        primaryKey = None
        fields = []
        mappings = dict()  # 用户类中的映射关系

        # 一个k, v 类似于 id : IntegerField('id')
        # 其中k是id，v是IntegerField的一个实例
        # 可以使用print(attrs)查看有哪些属性，帮助理解
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v # 保存映射关系
                # 如果是主键，判断是否只有一个主键
                if v.primary_key:

                    # 如果定义了多个主键，报错
                    if primaryKey:
                        raise Exception('Duplicate primary key for field: %s' % k)
                    primaryKey = k
                # 不是主键则添加到fields里
                else:
                    fields.append(k)

        # 如果所有属性里都没有主键，报错
        if primaryKey is None:
            raise BaseException('Primary key not found.')
        # 从类属性中删除该Field属性，否则容易造成运行时错误（实例的属性会遮盖类的同名属性）
        for k in mappings.keys():
            attrs.pop(k)

        # 数据库操作中有时候会遇到特殊的字段名或者表名，比如table name，存在空格。这时可以使用``，比如`table name`
        escaped_fields = list(map(lambda f: '`%s`' % f, fields)) # 关于map函数不再赘述，有问题可网上查找相关资料

        # 将获取到的数据作为类属性
        attrs['__mappings__'] = mappings      # 映射关系
        attrs['__table__'] = tableName         # 表名
        attrs['__primary_key__'] = primaryKey   # 主键
        attrs['__fields__'] = fields            # 除了主键外的字段

        # 提前设置好SQL语句的模板
        attrs['__select__'] = 'select `%s` , %s from `%s` ' % (primaryKey, ', '.join(escaped_fields), tableName)
        attrs['__insert__'] = 'insert into `%s` (`%s`,%s) values (%s)' % (tableName, primaryKey, ', '.join(escaped_fields), create_args_string(len(escaped_fields) + 1))
        attrs['__update__'] = 'update `%s` set %s where `%s`=? ' % (tableName, ', '.join(map(lambda f: '`%s` = ?' % (mappings.get(f).name or f), fields)), primaryKey)
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primaryKey)

        # 将拦截的类修改之后，返回新的类
        return type.__new__(cls, name, bases, attrs)

# 定义Model类，当用户如果需要与数据库交互，应当继承自该类
# 定义一些方法，用于某些数据库操作
# 父类是dict，方便操作，因为基本上都是字典数据
class Model(dict, metaclass=ModelMetaclass):

    # 如果子类没有实现__init__方法，会调用父类的__init__方法
    # 所以这里的kw实际上是子类在实例化的时候传入的参数
    # 比如定义一个User子类，对应数据库中的User表 User(id=123, name='Michael')
    # 那么父类Model的 **kw 接收的参数为 {'id':123,'name':'Michael'}
    def __init__(self, **kw):
        super().__init__(**kw)

    # 访问对象的key属性时，如果对象并没有这个相应的属性，那么将会调用__getattr__（）方法来处理
    def __getattr__(self, key):
        try:
            return self[key]   # Model类也是一个dict，具有dict的功能
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    # 当试图对对象的key赋值的时候将会被调用
    def __setattr__(self, key, value):
        self[key] = value

    # 返回key对应的值，没找到则返回None
    def getValue(self, key):
        return getattr(self, key, None)

    # 获取key对应的value，没找到则返回之前在字段中定义的默认值
    def getValueOrDefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]  # 这里之前保存的映射关系就用上了，value是Field类的某一个子类的实例
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default
                print('using default value for %s: %s' % (key, str(value)))
                setattr(self, key, value)
        return value

    # classmethod装饰器表示该类为类方法，无需创建实例即可调用，如Model.findAll()

    # 后面基本上就是实现关于数据库的方法，save, update, delete等。构造SQL语句，利用aiomysql实现异步执行操作。
    # 因为篇幅以及涉及到异步io的知识，所以不再详细分析，知道大致原理，可以尝试自己去编写后面部分

    @classmethod
    async def findAll(cls, where=None, args=None, **kw):
        ' find objects by where clause. '
        sql = [cls.__select__]
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        orderBy = kw.get('orderBy', None)
        if orderBy:
            sql.append('order by')
            sql.append(orderBy)
        limit = kw.get('limit', None)
        if limit is not None:
            sql.append('limit')
            if isinstance(limit, int):
                sql.append('?')
                args.append(limit)
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append('?, ?')
                args.extend(limit)
            else:
                raise ValueError('Invalid limit value: %s' % str(limit))
        rs = await select(' '.join(sql), args)  # 执行sql语句，该select()方法在代码最后实现，涉及异步的知识
        return [cls(**r) for r in rs]

    @classmethod
    async def findNumber(cls, selectField, where=None, args=None):
        sql = ['select %s _num_ from `%s`' % (selectField, cls.__table__)]
        if where:
            sql.append('where')
            sql.append(where)
        rs = await select(' '.join(sql), args, 1)
        if len(rs) == 0:
            return None
        return rs[0]['_num_']

    @classmethod
    async def find(cls, pk):
        rs = await select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])

    async def save(self):
        args = list(map(self.getValueOrDefault, self.__fields__))
        args.append(self.getValueOrDefault(self.__primary_key__))
        rows = await execute(self.__insert__, args)      # 执行sql语句，该execute()方法在代码最后实现，涉及异步的知识
        if rows != 1:
            print('failed to insert record: affected rows: %s' % rows)

    async def update(self):
        args = list(map(self.getValue, self.__fields__))
        args.append(self.getValue(self.__primary_key__))
        rows = await execute(self.__update__, args)
        if rows != 1:
            print('failed to update by primary key: affected rows: %s' % rows)

    async def remove(self):
        args = [self.getValue(self.__primary_key__)]
        rows = await execute(self.__delete__, args)
        if rows != 1:
            print('failed to remove by primary key: affected rows: %s' % rows)

# SQL语句的占位符是?，而MySQL的占位符是%s，select()函数在内部自动替换。
# 注意要始终坚持使用带参数的SQL，而不是自己拼接SQL字符串，这样可以防止SQL注入攻击。

# 创建连接池
# 详细教程参考 aiomysql官方文档
async def create_pool(loop, **kw):
    global __pool
    __pool = await aiomysql.create_pool(
        host = kw.get('host','localhost'),
        port = kw.get('port',3306),
        user = kw['user'],
        password = kw['password'],
        db = kw['db'],
        loop = loop
    )

# execute()函数和select()函数分开写，因为在execute()中cursor对象不返回结果集，而是通过rowcount返回结果数

async def select(sql, args, size=None):
    global __pool
    async with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?','%s'), args or ())
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
        return rs

async def execute(sql, args, autocommit=True):
    async with __pool.get() as conn:
        if not autocommit:
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(sql.replace('?', '%s'), args)
                affected = cur.rowcount
            if not autocommit:
                await conn.commit()
        except BaseException as e:
            if not autocommit:
                await conn.rollback()
            raise
        return affected
