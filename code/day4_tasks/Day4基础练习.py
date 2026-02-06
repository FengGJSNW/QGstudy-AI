# 基础学习

a = [i*i for i in range (1,11)]
print(a)

name = ["张三", "李四"]
name_QG = list(map(lambda i : 'QG_' + i, name))
print(name_QG)