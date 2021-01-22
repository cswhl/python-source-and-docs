# 当一些信息需要使用类似于字典套字典套列表这种很深的结构来储存的时候，请改用类来储存


class Person(object):
    def __init__(self, name='', age=0, sex='', detail=None):
        self._name = name
        self._age = age
        self._sex = sex
        self._detail = detail

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, new_sex):
        self._sex = new_sex

    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, new_detail):
        self._detail = new_detail


class Detail(object):
    def __init__(self, address='', work='', salary=0):
        self._address = address
        self._work = work
        self._salary = salary

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, new_address):
        self._address = new_address

    @property
    def work(self):
        return self._work

    @work.setter
    def work(self, new_work):
        self._work = new_work

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary


detail_kingname = Detail(address='xxx', work='engineer', salary=10000),
kingname = Person(name='kingname', age=23, sex='male', detail=detail_kingname)
detail_xiaoming = Detail(address='yyy', work='pm', salary=0.5),
xiaoming = Person(name='xiaoming', age=65, sex='male', detail=detail_xiaoming)
person_list = [kingname, xiaoming]
