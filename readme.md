# CIE Python语法考点总结

## 一. 基本变量声明与初始化

1. **常规变量类型**  
   系统自动检测类型
   ```python
   a = 1          # integer
   b = "abc"      # string
   c = True       # boolean
   ```

2. **各类型数组初始化**
   ```python
   a = [0] * 10       # 整数组，长度10，初始为0
   b = [""] * 10      # 字符串数组
   c = [None] * 10    # 空数组（常用于 Class）
   ```

3. **二维数组初始化**
   ```python
   #创建row行col列的二维数组
   arr = [[0 for _ in range(col)] for _ in range(rol)]
   brr = [["" for _ in range(col)] for _ in range(rol)]
   crr = [[None for _ in range(col)] for _ in range(rol)]
   ```

4. **日期**
   ```python
   from datetime import date #非标准库，因此需要导入
   d = date(2025, 3, 1) #创建日期对象，如date(2025, 3, 1)
   print(d.year, d.month, d.day) #date三个属性：year, month, day
   ```

5. **全局变量声明**
   ```python
   global Animals #声明全局数组
   Animals = [""] * 10 #存储10个动物名称的数组，必须与第一行分开写
   ```

6. **类型注释（CIE要求）**
   ```python
   QueueArray = []  # array of string
   HeadPointer = 0  # integer
   ```

7. **全局变量函数调用**
   ```python
   def function():
       global Animals #若要调用并操作要写这一行
       pass
   ```

---

## 二. 变量操作

1. **常规操作**
   ```python
   a, b = b, a       # 交换
   a is b            # 是否同一地址
   a = int(a)        # 转换为 int
   b = str(b)        # 转换为 str
   ```

   **运算符**：
   `加法：+`
   `减法：-`
   `乘法：*`
   `除法：/`
   `整除：//`
   `求余：%`
   `求幂：**`

2. **字符串**
   ```python
   len(s)                 # 长度
   s += "a"               # 追加
   "a" in s               # 判断是否包含
   s.find("a")            # 找索引，不存在返回 -1
   s.index("a")           # 找索引，不存在报错
   s[1:3], s[1:], s[:3]   # 切片
   f"my name is {name}"   # f-string 格式化
   s.strip()              # 去除首尾空白
   ```

3. **数组**
   ```python
   arr.append(x)
   del arr[2]             # 删除某位置
   a in arr               # 是否存在
   arr[i] = a             # 修改
   ```

---

## 三. 循环结构

1. **for 循环**
   ```python
   for i in range(num):
       pass

   for i in range(start, end):
       pass

   for i in range(start, end, step):
       pass
   ```

   嵌套：
   ```python
   for Row in range(1, 3):
       for Col in range(1, 9):
           pass
   ```

2. **while 循环**
   ```python
   while condition:
       pass

   while True:
       pass
       if condition:
           break
   ```

---

## 四. 函数

1. **基本定义**
   ```python
   def function(parameter):
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
   ```python
   def main():
       pass

   if __name__ == "__main__":
       main()
   ```

---

## 五. 类与 OOP

1. **定义与构造函数**
   ```python
   class Name:
       def __init__(self, aa, bb, cc):
           self.a = aa
           self.__b = bb
           self.__c = cc
       def geta(self):
           return self.a
       def seta(self, x):
           self.a = x
   ```

2. **继承**
   ```python
   class Names(Name):
       def __init__(self, a, b):
           Name.__init__(self, a)
           self.b = b
   ```

3. **重写方法**
   ```python
   class A:
       def f(self): pass

   class B(A):
       def f(self): pass
   ```

4. **对象数组**
   ```python
   CharacterArray = [None] * 5
   CharacterArray[0] = Character("Victory")
   ```

---

## 六. 文件操作与异常处理

1. **读取文件**
   ```python
   def ReadData():
       try:
           with open("Data.txt", "r") as f:
               DataArray = f.read().splitlines()
               Data = f.readline().strip()
           return DataArray
       except IOError:
           print("文件未找到")
           return []
   ```

2. **逐行读取**
   ```python
   file = open("file.txt", "r", encoding="utf-8")
   while True:
       s = file.readline()
       if not s:
           break
       print(s.strip())
   file.close()
   ```

---

## 七. 递归

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
   try:
       Answer = Num1 / (Num2 - 6)
   except ZeroDivisionError:
       print("除数不能为零")
   except Exception as e:
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
   Queue = [""] * 50
   HeadPointer, TailPointer = -1, 0

   def Enqueue(item):
       global TailPointer, HeadPointer
       if TailPointer >= len(Queue):
           return -1
       Queue[TailPointer] = item
       TailPointer += 1
       if HeadPointer == -1:
           HeadPointer = 0
       return 1
   ```

2. **随机数**
   ```python
   import random
   ArrayData[x][y] = random.randint(1, 100)
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
