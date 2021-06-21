#101
print("101 - 整數格式化輸出")
a = list() 
for i in range(0, 4):
    a.append(int(input()))
print("|%5d %5d|\n|%5d %5d|" % (a[0], a[1], a[2], a[3]))
print("|%-5d %-5d|\n|%-5d %-5d|" % (a[0], a[1], a[2], a[3]))

# 102
print("102 - 浮點數格式化輸出")
a = list() 
for i in range(0, 4):
    a.append(float(input()))
print("|%7.2f %7.2f|\n|%7.2f %7.2f|" % (a[0], a[1], a[2], a[3]))
print("|%-7.2f %-7.2f|\n|%-7.2f %-7.2f|" % (a[0], a[1], a[2], a[3]))

# 103
print("103 - 字串格式化輸出")
a = list() 
for i in range(0, 4):
    a.append(input())
print("|%10s %10s|\n|%10s %10s|" % (a[0], a[1], a[2], a[3]))
print("|%-10s %-10s|\n|%-10s %-10s|" % (a[0], a[1], a[2], a[3]))

# 104
print("104 - 圓形面積計算")
import math
r = eval(input())
print("Radius = %.2f" % r)
print("Perimeter = %.2f" % (r * 2 * math.pi))
print("Area = %.2f" % (r * r * math.pi))


# 105
print("105 - 矩形面積計算")
h = eval(input())
w = eval(input())
print("Height = %.2f" % h)
print("Width = %.2f" % w)
print("Perimeter = %.2f" % ((h + w) * 2))
print("Area = %.2f" % (h * w))

# 106
print("106 - 公里英哩換算")
x = float(input())
y = float(input())
z = float(input())
print("Speed = %.1f" % ((z/1.6) / ((x + y / 60) / 60)))

# 107
print("107 - 數值計算")
a = list()
total = 0
for i in range(0, 5):
    a.append(eval(input()))
    total += a[i]
print(a[0], a[1], a[2], a[3], a[4]) 
print("Sum = %.1f" % total)
print("Average = %.1f" % (total / 5))

# 108
print("108 - 座標距離計算")
import math
x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())
print("( " + str(x1) + " , " + str(y1) + " )\n( " + str(x2) + " , " + str(y2) + " )")
print("Distance = %.4f" % (math.sqrt((x1 -x2) ** 2 + (y1 - y2) ** 2)))

# 109
print("109 - 正五邊形面積計算")
import math
s = eval(input())
print("Area = %.4f" % ((5 * s**2) / (4 * math.tan(math.pi / 5))))

# 110
print("110 - 正n邊形面積計算")
import math
n = eval(input())
s = eval(input())
print("Area = %.4f" % ((n * s**2) / (4 * math.tan(math.pi / n))))