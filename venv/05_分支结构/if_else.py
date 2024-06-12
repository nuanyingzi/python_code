height = float(input("请输入您的身高（cm）："))
weight = float(input("请输入您的体重（kg）："))

bmi = weight / (height / 100) ** 2
print("bmi is %.1f" % bmi)

if bmi < 18.5:
    print("您的身材过轻")
elif bmi < 24:
    print("您的身材很不错")
else:
    print("废物，少吃点")