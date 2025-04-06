class person:
    def Details(self,name,age,salary):
        self.name = name
        self._age = age
        self.__salary = salary
    
    def info(self):
        print("Name :",self.name)
        print("Age :",self._age)
        print("Salary :",self.__salary)
        
    def getSalary(self):
        return self.__salary
    
    def setSalary(self,Salary):
        self.__salary = Salary
        
P = person()
P.Details("Ahkalya",21,50)
P.info()
print("GetSAlary:",P.getSalary())
P.setSalary(500)
P.info()
    