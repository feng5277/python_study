# BMI = 体重 / （身高 ** 2）
#input采集到的输入默认是字符串类型，如果需要用它来运算则需要使用float()函数来转换数据类型
user_height = float(input("你的身高是（单位：m）："))
user_weight = float(input("你的体重是（单位：kg）："))
user_BMI = user_weight / (user_height ** 2)
print("您的BMI是：" + str(user_BMI))  # print输出时字符串只能和字符串一起输出，因此需要str()来把浮点型转成字符串
# 数据类型转换演示
a = "527"
print(type(a))
a = float (a) # 注意此处需要把结果赋值给a
print(type(a))

# 多条件判断——接上文的BMI判断
if user_BMI < 18.5:
    print("偏瘦")
elif 18.5 <= user_BMI <= 25: # 多条件判断用elif
    print("正常")
else:
    print("偏胖")

# 条件语句
mood_index = int(input("请输入女友今天的心情："))
if mood_index >= 60:
    print("可以打游戏！")
else:
    print("不可以打游戏")
    