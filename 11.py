# 高阶函数与匿名函数
def calculate_anf_print(num,calculator):
    result = calculator(num)
    print(f"原始参数：{num},计算结果：{result}")

def calculate_square(num):
    return num * num
def calculate_cube(num):
    return num * num * num
def calculate_plus_10(num):
    return num + 10
def calculate_times_5(num):
    return num * 5

calculate_anf_print(5,calculate_square) # 可以将函数作为变量传入另一个函数


def calculate_anf_print1(num,calculator,formatter):
    result = calculator(num)
    formatter(num,result)
def print_with_vertical_bar(num,result):
    print(f"原始参数：{num},计算结果：{result}")

def calculate_square(num):
    return num * num
def calculate_cube(num):
    return num * num * num
def calculate_plus_10(num):
    return num + 10
def calculate_times_5(num):
    return num * 5
"""格式化函数也可以作为高阶函数的参数传入"""
calculate_anf_print1(8,calculate_square,print_with_vertical_bar)

# 匿名函数
calculate_anf_print1(8,lambda num: num **3,print_with_vertical_bar)

result = (lambda m1, m2: m1 * m2)(5,6)
print(result)