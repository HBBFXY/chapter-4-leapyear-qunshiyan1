year = input()
try:
    year = int(year)
    if year <= 0:
        print("输入错误，请输入大于0的整数")   
    else:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print("是闰年")
        else:
             print("不是闰年")
except ValueError:
    print("输入错误")
