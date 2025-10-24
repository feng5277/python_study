# python打开文件
f = open("./test.txt","r",encoding="utf-8") # “r”代表读取模式/“w”代表写入模式（会覆盖原本的内容）/“a”代表附加模式（在末尾写入）
content = f.read()
print(content)
f.close()

with open("./test.txt","r",encoding="utf-8") as f:
    content = f.read()
    print(content)

with open("./test.txt","r",encoding="utf-8") as f:
    print(f.readline())
    print(f.readline())
    print(f.readlines())

with open("./test.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line)

# r+ 模式用于以读写方式打开文件。文件必须已存在，写操作会从文件开头开始，覆盖对应字符
# r+ 打开文件时指针默认在文件开头，因此直接 read() 可以读取全部内容。
# 写入时，内容会从当前指针位置开始覆盖（不会自动跳转到末尾），若指针在中间，会覆盖原有内容；若指针在末尾，则相当于追加。
# a+ 模式用于以追加读写方式打开文件。如果文件不存在，则创建新文件；如果文件已存在，写操作会从文件末尾开始。
# a+ 打开文件时指针默认在文件末尾（同 a 模式），因此直接 read() 会读不到内容。
# 需手动通过 seek(0) 将指针移到开头才能读取内容；但写入时，指针仍会自动跳回末尾（强制追加，无法覆盖原有内容）。
# 我欲乘风归去⑺，又恐琼楼玉宇⑻，高处不胜寒⑼。起舞弄清影⑽，何似在人间
with open("./poem.txt","w",encoding="utf-8") as file:
    file.write("我欲乘风归去，\n又恐琼楼玉宇。\n高处不胜寒，\n起舞弄清影。\n")
with open("./poem.txt","a+",encoding="utf-8") as f:
    f.seek(0)
    content = f.read()
    print(content)
    f.write("何似在人间。")
    f.seek(0) # 将指针调整到最开始的位置。read只会读取指针后面的内容
    print(f.read())

# with open("test.txt", "r+", encoding="utf-8") as f:
#     f.seek(7)  # 移动指针到第7个字节（字符 'w' 处）
#     f.truncate()  # 截断：保留指针前的内容，删除后续内容