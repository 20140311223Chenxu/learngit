class Student(object):
    pas
>>> s = Student()
>>> s.name = 'Michael' # ��̬��ʵ����һ������
>>> print(s.name)
Michael
>>> def set_age(self, age): # ����һ��������Ϊʵ������
...     self.age = age
...
>>> from types import MethodType
>>> s.set_age = MethodType(set_age, s) # ��ʵ����һ������
>>> s.set_age(25) # ����ʵ������
>>> s.age # ���Խ��
25
>>> s2 = Student() # �����µ�ʵ��
>>> s2.set_age(25) # ���Ե��÷���
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'set_age'