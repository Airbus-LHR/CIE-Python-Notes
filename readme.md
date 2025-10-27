# CIE Python语法考点总结

## 一. 基本变量声明与初始化

1. **常规变量类型**
   
   系统自动检测类型
   ```python
   a = 1 #integer
   b = "abc" #string
   c = True #boolean
   ```

3. **各类型数组声明及初始化**
   ```python
   a = [0] * 10 #整数组，长度10，初始为0
   b = [""] * 10 #字符串数组
   c = [None] * 10 #空数组（常用于 Class）
   d = [] #不做任何初始化，若题目不要求初始化则这样写
   ```

4. **二维数组初始化**
   ```python
   #创建row行col列的二维数组
   arr = [[0 for _ in range(col)] for _ in range(rol)] #初始化为0
   brr = [["" for _ in range(col)] for _ in range(rol)] #字符串初始化""
   crr = [[None for _ in range(col)] for _ in range(rol)] #初始化空
   drr = [[for _ in range(col)] for _ in range(rol)]
   ```

5. **日期**
   ```python
   from datetime import date #非标准库，因此需要导入
   d = date(2025, 3, 1) #创建日期对象，如date(2025, 3, 1)
   print(d.year, d.month, d.day) #date三个属性：year, month, day
   ```

6. **全局变量声明**
   ```python
   global Animals #声明全局数组
   Animals = [""] * 10 #存储10个动物名称的数组，必须与第一行分开写
   ```

7. **全局变量函数调用**
   ```python
   def function():
       global Animals #若要调用并操作要写这一行
       pass
   ```

8. **类型注释（CIE要求）**
   ```python
   QueueArray = [] #array of string
   HeadPointer = 0 #integer
   ```

8. **类型检测**
   
   ·使用type()函数
   ```python
   a = 1
   b = ""
   type(a) is int #判断a是否为int
   type(b) is not str #判断b是否不为str
   ```

---

## 二. 变量操作

1. **常规操作**
   ```python
   a, b = b, a #交换
   a is b      #是否同一地址
   a = int(a)  #转换为 int
   b = str(b)  #转换为 str
   ```

   *运算符*：
   `加法：+`
   `减法：-`
   `乘法：*`
   `除法：/`
   `整除：//`
   `求余：%`
   `求幂：**`

2. **字符串**
   ```python
   len(s) #长度
   s += "a" #追加
   "a" in s #判断是否包含
   s.find("a") #找索引，不存在返回 -1
   s.index("a") #找索引，不存在报错
   s[1:3], s[1:], s[:3] #切片，左闭右开
   f"my name is {name}" #f-string 格式化字符串
   s.strip() #去除首尾空白
   s.casefold() #忽略大小写，也可以统一用lower()
   s.lower() #返回全小写
   a > b #字母顺序比较，越大越靠后
   ```

3. **浮点数**
   ```python
   import math
   a == b #会返回false因为会有舍入误差
   a - b < 0.0001 #正确方法：控制精度误差
   round(a, 2) #保留两位小数
   math.ceil(a) #向上保留两位小数
   math.floor(a) #向下保留两位小数
   print(f"{x:.2f}") #格式化字符串显示
   ```

4. **数组**
   ```python
   arr.append(x) #追加
   del arr[2] #删除某位置
   a in arr   #是否存在
   arr[i] = a #修改
   ```

---

## 三. 分支结构与循环结构

1. **分支结构**
   ·使用if语句（常规分支结构）
   ```python
   if a == 1:
       print('yes')
   elif a == 2:
       print('no')
   else:
       print('?')
   ```
   
   ·快速判断是否为某些值（不用写多个if）
   ```python
   if a in ['1', '4', '5', '8', '9']: #不用写5个if或者多重or
       print(1)
   ```

   ·match case语句
   ```python
   a = int(input())
   match a:
       case 1 | 0:
           print('a')
       case 2:
           print('b')
       case 3:
           print('c')
       case _: #else语句
           print('else')
   ```
2. **for 循环**
   ```python
   for i in range(num): #循环num次
       pass

   for i in range(start, end): #循环end-start次，包start不包end
       pass

   for i in range(start, end, step): #执行循环，从start至end，步长为step（P4不常考）
       pass
   for i in arr: #遍历每个元素，此时i表示的是元素不是索引，相当于Java的for each loop
       print(i)
   for i in Node:
       print(i.data)
   ```
   
   **嵌套：**
   ```python
   for Row in range(1, 3): #行范围
       for Col in range(1, 9): #列范围
           pass
   ```

3. **while 循环**
   ```python
   while condition: #只要condition成立
       pass
   ```
   **注：Python无do后置条件循环**
   ·死循环用法（用于暂时写不出具体条件）
   ```python
   while True:
       pass
       if condition:
           break
   ```

---

## 四. 函数

1. **基本定义**
   ```python
   def function(parameter): #依旧自动检测参数类型，类型与操作不匹配会报错
       return 1
   ```

2. **函数嵌套**
   ```python
   def a(x):
       def b(y):
           pass
       return b(x)
   ```

3. **主函数写法**
   方法1：直接写
   方法2：
   ```python
   def main():
       pass
   
   if __name__ == "__main__": #函数结束后在末尾加上这两行
       main()
   ```

---

## 五. 类与 OOP

1. **定义与构造函数**
   ```python
   class Name: #类名
       def __init__(self, aa, bb, cc): #构造器
           self.a = aa #公有属性
           self.__b = bb #私有属性前面加__
           self.__c = cc
       def funa(): #定义其他函数，但必须加self传参，无其他传参也得加
           pass
       def geta(self): #常见getter
           return self.a
       def seta(self, x): #常见setter
           self.a = x
   ```

2. **继承**
   ```python
   class Names(Name): #括号内为继承的父类
       def __init__(self, a, b):
           super().__init__(a) #调用父类构造器
           self.b = b
   ```

3. **重写方法**
   ```python
   class A:
       def f(self): pass

   class B(A): #直接写，系统直接覆盖
       def f(self): pass
   ```

4. **对象数组**
   ```python
   CharacterArray = [None] * 5
   CharacterArray[0] = Character("Victory")
   ```

---

## 六. 文件操作

1. **读取文件**
   ```python
   def ReadData():
       try:
           with open("Data.txt", "r") as f: #读取文件名，r为只读模式，w为写模式，with后自动关闭文件
               DataArray = f.read().splitlines() #按行读取，执行一次读取一行
               Data = f.readline().strip() #读一行并去掉空白首尾
           return DataArray
       except IOError:
           print("文件未找到")
           return []
   ```

2. **逐行读取**
   若不知道有多少行/一次要读多行：
   ```python
   file = open('D:\Sunny\计算机\Python语法考点.txt', "r", encoding="utf-8") #若文件不在源代码同级文件夹内需要写出完整路径
   while True:
       s = file.readline()
       if not s:
           break
       print(s.strip())
   file.close()
   ```

---

## 七. 递归
**函数主体示例**
```python
def recursion(a):
    if base:
        return 1
    return recursion(a - 1)
```

例：二分查找
```python
def BinarySearch(arr, low, high, target):
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return BinarySearch(arr, low, mid - 1, target)
        else:
            return BinarySearch(arr, mid + 1, high, target)
    return -1
```

---

## 八. 异常处理

1. **捕获异常**
   ```python
   try: #常规操作
       Answer = Num1 / (Num2 - 6)
   except ZeroDivisionError: #异常1
       print("除数不能为零")
   except Exception as e: #异常2
       print(f"错误: {e}")
   ```

2. **手动抛出**
   ```python
   raise TypeError
   ```

---

## 九. 其他重点

1. **队列实现**
   ```python
   Queue = [""] * 50 #存储50个字符串
   HeadPointer, TailPointer = -1, 0 #队首指针（初始-1）队尾指针（初始0）

   def Enqueue(item): #入队函数
       global TailPointer, HeadPointer
       if TailPointer >= len(Queue):
           return -1 #队列已满
       Queue[TailPointer] = item
       TailPointer += 1
       if HeadPointer == -1: #首次入队
           HeadPointer = 0
       return 1
   ```

2. **随机数生成**
   ```python
   import random
   ArrayData[x][y] = random.randint(1, 100) #生成1-100的随机整数
   ```

3. **冒泡排序**
   ```python
   def BubbleSort(ArrayData):
       n = len(ArrayData)
       for i in range(n-1):
           for j in range(0, n-i-1):
               if ArrayData[j] > ArrayData[j+1]:
                   ArrayData[j], ArrayData[j+1] = ArrayData[j+1], ArrayData[j]
       return ArrayData
   ```