#""中间的空格会输出
#“+”可以连接两个打印的字符串
print("你好" + " 这是一行代码" + " 哈！")

#"\"是转义字符，其后的符号会被认为是单纯的符号
print('Let\'s go')

#“\n”代表的是换行
print("明天我们一起去书店\n买书")

#“三个引号”包裹的文字可以按照原本的输出形式打印
print("""床前看月光，
疑是地上霜。
举头望山月，
低头思故乡""")

#定义变量
great = "v我50，"
print(great + "王五")
great_chinese = great
great_english ="v me 50"
great = great_english
print(great + "李六")

#导入math库来进行数学中的求根公式运算，math.sqrt是开根号运算
import math
a = 1
b = 8
c = 3
print(math.sqrt(b ** 2 - 4 * a * c) / (2 * a))
print(math.sqrt(b ** 2 + 4 * a * c) / (2 * a))
print(math.log2(8))

#字符串操作
print(type(None))
s = "hello world!"
k = " 6 "
print(type(s))
print(len(s))
print(type(k))
print(len(k))
#通过索引获得单个字符
print(s[0])
print(s[11])
print(s[-1])

#布尔类型
b1 = True
b2 = False

# 空值类型
n = None

#type函数
print(type(b1))
print(type(n))
print(type(2.3))
