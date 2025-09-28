import pickle
import datetime
class Student:
    def __init__(self):
        self.name = ""
        self.registerNumber = 0
        self.dateOfBirth = datetime.datetime.now()
        self.fullTime = True
studentRecord = Student()
studentFile = open("students.dat", 'wb')
print("Please enter student details:")
studentRecord.name = input("Please enter student name: ")
studentRecord.registerNumber = int(input("Please enter student's register number: "))
year = int(input("Enter year of birth YYYY: "))
month = int(input("Enter month of birth MM: "))
day = int(input("Enter day of birth DD: "))
studentRecord.dateOfBirth = datetime.datetime(year, month, day)
studentRecord.fullTime = bool(input("Please enter True for full-time or False for part-time: "))
pickle.dump(studentRecord, studentFile)
print(studentRecord.name, studentRecord.registerNumber, studentRecord.dateOfBirth, studentRecord.fullTime)
studentFile.close()
studentFile = open("students.dat", 'rb')
studentRecord = pickle.load(studentFile)
print(studentRecord.name, studentRecord.registerNumber, studentRecord.dateOfBirth, studentRecord.fullTime)
studentFile.close()