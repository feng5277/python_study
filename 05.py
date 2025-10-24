# 格式化字符串方法
# 01:format方法
name = "老李"
gap = 3.665
message_content = """
{0}你好
你的绩点为{1:04.1f}""".format(name, gap)
# f：用于浮点型变量的格式化。
# 04.1f 中：0 表示不足长度时补 0；4 是总长度（含整数、小数点、小数）；.1 表示保留 1 位小数。
print(message_content)
# 变形：
message_content = """
{p}你好
你的绩点为{k:.1f}""".format(p = name, k = gap) #此处p和k不能替换成0和1因为此种方法占位符是变量，而变量不能以数字开头去命名
print(message_content)

# 02:f求值法(字符串前面加f会对字符串中的大括号中的内容求值)
essage_content = f"""
{name}你好
你的绩点为{gap:.1f}"""
print(essage_content)

# 定义BMI计算函数
def calculate_BMI(height, weight):
    BMI = weight / height ** 2
    if BMI < 18.5:
        category = "偏瘦"
    elif BMI >= 18.5 and BMI < 25:
        category = "正常"
    else:
        category = "偏胖"
    print(f"您的体型为{category}")
    return BMI
calculate_BMI(1.7,45)
print(calculate_BMI(1.7,55)) # return出来的结果只是赋值了，需要打印才能打印出来