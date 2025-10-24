# 逻辑运算（优先级：not > and > or）
a = 3
b = 6
c = 5
if (a > 2 and b > 5 and not c >10):
    print("527")

# 列表
price = [100, 512, 527]
price.append(666)
print(price)
price.remove(100)
print(price) #pytorch
print(len(price))
print(price[-1])
price[0] = 689
print(price)
print(max(price))
print(min(price))
print(sum(price))
print(sorted(price))

# 字典，用来存储键值对（键是用来查找的索引）
# 注：键的类型必须是不可变的，因此不能是列表（列表为可见的），但是可以是元组
example_tuple = (1, 2, 3) # 此为元组
example_list = [1, 2, 3] #此为列表
print(type(example_tuple))
# 字典示例（电话本）
contacts = {"老李":"1278687631",
            "老张":"8657867554",
            "老陈":"98475280465"}
contacts["小花"] = "789243758097"
print(contacts)
print("老李" in contacts)
del contacts["老李"]
print("老李" in contacts)
query = input("请输入要查询的联系人：")
if query in contacts:
    print(query + "的电话为：" + contacts[query])
else:
    print("查询的对象不在通讯录中，目前已收录联系人数量为" + str(len(contacts)) + "人")

# 字典拓展方法
temperature_dict = {"01":36.5,
                    "02":38.0,
                    "03":37.0,} # 注意键都是字符串，需要加引号
temperature_dict.keys()     # 代表所有键
temperature_dict.values()   # 代表所有值
temperature_dict.items()    # 代表所有键值对




