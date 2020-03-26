# 判断  代码块  缩进
# a = 1
# b = 2


# if a ==1:
#     print("哈哈哈哈")


# if a > b:
#     print("a比b大")
# else:
#     print("b更大")

# age = int(input("请输入你的年龄："))
# if age > 60:
#     print("你应该退休了")
# elif age > 30:
#     print("家庭的责任很重吧")
# elif age > 20:
#     print("一定要好好规划你的未来！")
# else:
#     print("读书的时候，要认真！89")

# if age > 20 and age <=30:
#     print("2222")
# elif age > 30:
#     print("3333")
# elif age > 60:
#     print("44444")
# else:
#     print("xxxxxx")

# a = "asdfg"
# if type(a) is int:
#     print("是数字")
# elif type(a) is str:
#     print("是字符串")
# else:
#     print("其他")

# a = 1
# while a < 10:
#     print("哈哈哈哈")
#     a = a + 1

# 现在有10个学生成绩需要录入到系统中，这是个人分别是 张三  李四  王马  流云 浪晋 希希 朱朱 雅素 二狗 小亮
#并且名字和成绩需要对应上 而且大于和小于60的需要分开存放


# input
# 数组/字典

# a = input
# print(a)
# dict

# highchengji = {}
# lowchengji = {}
# studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
# a = 0
# while a < len(studentlist):
#     chengji = int(input("请输入"+studentlist[a]+"的成绩："))
#     if chengji >=60:
#         highchengji[studentlist[a]] = chengji
#     else:
#         lowchengji[studentlist[a]] = chengji
#     a = a+1
# print("大于60的：",highchengji)
# print("小于60的：",lowchengji)

# studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
# for i in studentlist:
#     print(i)

# b = list(range(0,100,2))  # 自动生成了一个数组,步进/步长
# print(b)

# 练习：打印九九乘法表
