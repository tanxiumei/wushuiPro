
print(type(100))#type（） 查看类型
print(round(3.145263,4)) #取小数有效位
print(9/4)  #/可以除尽，等于2.25，不是只取整数部门，总是得到小数
print(9//4)  #//表示除法只取整数，等于2，小数部分不管

print(9%4)  #%取余数，余数为1，等于1
print(2**4)  #求次方，等于16
#可执行某几句代码，选中要运行的代码，然后右击，execute selection in python console
print("""三个双引号也是字符串""")
print('''三个单引号也是字符串''')
print('单引号是字符串')
print("双引号是字符串")
# 先入为主的原则,下面两个句子报的错误不一样
# 所有的数据类型都是对象
# print("hello" + 2)
#print(2+"hello")

import keyword
print(keyword.kwlist)#打印出python所有的关键字

#ctl+/  选中语句，可以注释或者取消注释
print(id(100))#查看地址