# 引入模块01
import statistics
print(statistics.median([12, 52, 3]))
print(statistics.mean([12, 52, 3]))
# 引入模块02
from statistics import median, mean
print(median([12, 52, 3]))  # 使用from*import*就不用再加模块.的前缀
print(mean([12, 52, 3]))

# 创建类以及对象
class CuteCat:
    def __init__(self,cat_name,cat_age,cat_color):
        self.cat_name = cat_name
        self.cat_age = cat_age
        self.cat_color = cat_color
cat1 = CuteCat("奇奇","5","pink")
print(f"小猫的名字是{cat1.cat_name}，年龄为{cat1.cat_age}岁，颜色是{cat1.cat_color}色。")

# 在类中创建方法
class Student:
    def __init__(self,name,student_id):
        self.name = name
        self.id = student_id
        self.grade = {"语文":0,"数学":0,"英语":0}
    def set_score(self,course,grade):
        if course in self.grade:
            self.grade[course] = grade
    def print_grade(self):
        print(f"{self.name}同学(学号{self.id}),您的成绩为：")
        for course in self.grade:
            # print(f"{course}:{self.grade[course]}分")
            print(course,self.grade[course])
chen = Student("chen",200155)
print(chen.grade)
chen.set_score("数学","100")
print(chen.grade)
chen.print_grade()
