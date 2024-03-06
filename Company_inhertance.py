''' Task - Some companies collecting their employees details with some conditions
 Companies - TCS, HCL, Infy
 Company need employees id, name, salary, location, age
 Condition for TCS: Specify a salary with 2 floating point
                     Show location = siruseri( By default), chennai
                     date of birth
                     Show Id with prefix 'TCS23' 
 Conditions for HCL: Show first name only if they have firstname, last name
                     Show the salary after 10 percent of detection
                     Show gender, Blood Group, Date of Birth
                     Show Id with prefix 'HCL23'
 Conditions for Infy: Show Experience, Mobile number, Address, Aadhar number
                     Show the salary as per annual salary
                     Show Id with prefix 'Infy23' '''
                     
#Code
class emp:
    def __init__ (self, ID, name, salary, location, age):
        self.ids = ID
        self.name = name
        self.salary = salary
        self.location = location
        self.age = age
    def show(self):
        print("\nHi my id is:",self.ids,"\nName: ", self.name,"\nSalary: ",
              self.salary,"\nLocation: ", self.location, "\nAge: " ,self.age)
    def salary_hike(self):
        self.salary = round(self.salary,2)

class TCS(emp):
    def __init__ (self, ID, name, salary, location, age, dob):
        super().__init__(ID, name, salary, location, age)
        self.dob = dob
        self.location = 'Siruseri'
    def show(self):
        print("\nHi my TCS id is:","TCS23"+str(self.ids), "\nName: ",self.name,
              "\nSalary: ",self.salary, "\nAge: ",self.age, "\nlocation: ",
              self.location, "\nDOB: ",self.dob)
    def salary_hike(self):
        self.salary = format(self.salary, '.2f')

class HCL(emp):
    def __init__ (self, ID, name, salary, location, age, gender, bloodgroup , doj, last_name):
        super().__init__(ID, name, salary, location, age )
        self.gender = gender
        self.bloodgroup = bloodgroup
        self.doj = doj
        self.last_name = last_name

    def show(self):
        Id = "HCLS23"+str(self.ids)
        print("\nHi my HCL id is:",Id,"\nName: ",self.name, self.last_name,
              "\nSalary: ",self.salary, "\nAge: ", self.age,  "\nLocation: ",self.location,
              "\nGender: ",self.gender, "\nBloodGroup: ",self.bloodgroup,"\nDOJ: ", self.doj)
    def salary_hike(self):
        self.salary = self.salary - (round(self.salary/10))
    
        
class Infy(emp):
    def __init__(self, ID, name, salary, age, location, mobile, Exp, address, aadhar):
        super().__init__(ID, name, salary, age, location)
        self.exp = Exp
        self.mobile = mobile
        self.address = address
        self.aadhar = aadhar
    def show(self):
        print("\nHi my Infy id is:","Infy23"+str(self.ids),"\nName: ", self.name,
              "\nSalary: ", self.salary, "\nAge: ",self.age, "\nLocation: ",self.location,  
              "\nMobile: ",self.mobile, "\nExp: ",self.exp, "\nAddress: ",self.address,
              "\nAadhar: ", self.aadhar)
    def salary_hike(self):
        self.salary = (self.salary)*12
        
        
e = emp(20, 'sarath', 30000, 'Salem', 28)
e.show()

e1 = TCS(1400, 'Varun', 30000, 'Salem', 22, '28/09/1999')
e1.salary_hike()
e1.show()

e2 = HCL(143, 'Sheela', 30000, 'Coimbatore', 25, 'F', 'A+', '22/09/2021', 'Vishwa')
e2.salary_hike()
e2.show()

e3 = Infy(2024, 'Lavanya', 30000, 'Madurai', 24, 6380783797, 2, '47, Madurai', '7417 XXXX XXXX')
e3.salary_hike()
e3.show()


# OUTPUT  

Hi my id is: 20 
Name:  sarath 
Salary:  30000 
Location:  Salem 
Age:  28

Hi my TCS id is: TCS231400 
Name:  Varun 
Salary:  30000.00 
Age:  22 
location:  Siruseri 
DOB:  28/09/1999

Hi my HCL id is: HCLS23143 
Name:  Sheela Vishwa 
Salary:  27000 
Age:  25 
Location:  Coimbatore 
Gender:  F 
BloodGroup:  A+ 
DOJ:  22/09/2021

Hi my Infy id is: Infy232024 
Name:  Lavanya 
Salary:  360000 
Age:  24
Location:  Madurai 
Mobile:  6380783797 
Exp:  2 
Address:  47, Madurai 
Aadhar:  7417 XXXX XXXX
