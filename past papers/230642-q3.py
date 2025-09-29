class Employee:
    def __init__(self, h, e, j):
        self.__HourlyPay = h #float
        self.__EmployeeNumber = e #string
        self.__JobTitle = j #string
        self.__PayYear2022 = [0.0] * 51 #array of float
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    def SetPay(self, w, n):
        pay = self.__HourlyPay * n
        self.__PayYear2022[w] = pay
    def getTotalPay(self):
        total = 0
        for i in range(len(self.__PayYear2022)):
            total += self.__PayYear2022[i]
        return total

class Manager(Employee):
    def __init__(self, h, e, j, b):
        Employee.__init__(self, h, e, j)
        self.__BonusValue = b #float
    def SetPay(self, w, n):
        n *= 1 + self.__BonusValue / 100
        Employee.SetPay(self, w, n)

global EmployeeArray
EmployeeArray = [None] * 8

def EnterHours():
    with open('HoursWeek1.txt', 'r', encoding = 'utf-8') as f:
        while True:
            n = f.readline().strip()
            h = f.readline().strip()
            if not h or not n:
                break
            for i in range(len(EmployeeArray)):
                if EmployeeArray[i].GetEmployeeNumber() == n:
                    EmployeeArray[i].SetPay(1, float(h))

def main():
    global EmployeeArray
    idx = 0
    with open('Employees.txt', 'r', encoding = 'utf-8') as f:
        while True:
            p = f.readline().strip()
            n = f.readline().strip()
            t = f.readline().strip()
            if not p or not n or not t:
                break
            if not (t[0] > '9' or t[0] < '0'):
                b = f.readline().strip()
                EmployeeArray[idx] = Manager(float(p), n, b, float(t))
            else:
                EmployeeArray[idx] = Employee(float(p), n, t)
            idx += 1
    EnterHours()
    for i in range(len(EmployeeArray)):
        print(EmployeeArray[i].GetEmployeeNumber())
        print(EmployeeArray[i].getTotalPay())

if __name__ == "__main__":
    main()
