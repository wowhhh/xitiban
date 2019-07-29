## 定义一个学生类
class Student(object):

    def __init__(self,name,age,scores):
        self.name = name
        self.age = age
        self.scores = scores
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return max(self.scores)
stu  = Student("wyb",18,(3,5,6))
print(stu.get_age())
print(stu.get_name())
print(stu.get_course())