temperature_dict = {"01":36.5,
                    "02":38.0,
                    "03":37.0,} # 注意键都是字符串，需要加引号
for staff_id, temperature in temperature_dict.items():
    if temperature > 37.0:
        print(staff_id + "发烧了！")


# print(staff_id, + "发烧了！")
# 对比维度	逗号 ,（print 函数的参数分隔符）	加号 +（字符串拼接运算符）
# 作用本质	分隔 print 函数的多个独立参数	对两个字符串进行 “合并运算”，生成新字符串
# 使用条件	无需考虑参数类型（可以是字符串、数字、列表等）	必须保证 + 两边都是字符串类型（否则报错）
# 输出效果	会自动在多个参数之间添加一个空格	直接将两个字符串 “无缝拼接”，没有额外空格
# 典型示例	print("年龄", 25) → 输出 年龄 25	print("年龄" + str(25)) → 输出 年龄25

# 高斯加法
total = 0
for i in range(1,101): # 注意range不会导出范围最后的那个数字
    total += i
print(total)

# 打印1到11中的所有奇数
#注意range只能处理整数，所以步长也不能出现浮点数
for i in range(1,12,2):
    print(i)

# 利用while写一个求平均值计算器
print("hello,我是一个求平均值的程序")
count = 0
total = 0
user_input = (input("请输入需要求平均值的数字（输入q结束）："))
while user_input != "q":
    number = float(user_input)
    count += 1
    total += number
    user_input = (input("请输入需要求平均值的数字（输入q结束）："))
if total == 0:
    print(0)
else:
    print("输入数字的平均值为:",total/count)
