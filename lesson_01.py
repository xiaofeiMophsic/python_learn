# lesson_01.py
# -*- coding: UTF-8 -*-
"""
    first python lesson
"""


class People:
    country = "中国";

    _name = "bob";
    _age = 10;

    @classmethod
    def get_country(cls):
        return People.country;

    # constructor for People
    def __init__(self, name, age):
        self._name = name;
        self._age = age;

    def __del__(self):
        self._name = "";
        self._age = 0;

    def get_name(self):
        return self._name;

    def get_age(self):
        return self._age;


class Student(People):
    stu_id = 123456;

    def get_stu_id(self):
        return self.stu_id;

    def set_stu_id(self, value):
        self.stu_id = value;

p = People("goda", 23);
p.address = "beijing";

print(p.get_name(), p.get_age(), p.address, p.get_country(), People.get_country(), People.get_age(p))
#############################################

s = Student("zhangsan", 20);
s.set_stu_id(11000);

print(s.get_name(), s.get_age(), s.get_stu_id());