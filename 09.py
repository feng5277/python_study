# 异常处理与捕捉
try:
    user_weight = float(input("请输入你的体重（kg）："))
    user_height = float(input("请输入你的身高（m）：")) # 有可能产生错误的代码
    BMI = user_weight / (user_height * user_height)
except ValueError: # 产生值错误时会运行
    print("输入不为合理的数字，请重新运行程序，并输入合理的数字。")
except ZeroDivisionError: # 产生除零错误时会运行
    print("身高不能为0，请重新运行程序，并输入正确的数字")
except: # 产生其他错误时会运行
    print("发生未知错误，请重新启动程序。")
else: # 没有错误时会运行
    print("您的BMI值为：" + str(BMI))
finally: # 不管是否发生错误都会运行
    print("程序运行结束")
