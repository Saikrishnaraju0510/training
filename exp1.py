def addnum(n1,n2):
    print(n1+n2);

def print0ton(num):
    for i in range(num):
        print(i);

class number():
    def __init__(self,name,phnumber,salary):
        self.name=name
        self.phnumber=phnumber
        self.salary=salary
    def getdata(self):
        print("{} earns {} rupees per month. contact him at {}".format(self.name,self.salary,self.phnumber))
    def highsalary(self,s2,s3):
        if(self.salary>s2.salary and self.salary>s3.salary):
            print("{} earns more than {} and {}".format(self.name,s2.name,s3.name))
        elif(s2.salary>s3.salary):
            print("{1} earns more than {0} and {2}".format(self.name,s2.name,s3.name))
        else:
            print("{2} earns more than {0} and {1}".format(self.name,s2.name,s3.name))

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b

def findprime(n):
    for i in range(2,n):
        if(n%i==0):
            print("{} is not a prime number".format(n))
            break
        else:
            print("{} is a prime number".format(n))
        
        
