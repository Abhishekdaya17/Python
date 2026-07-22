from collections import namedtuple
Emp = namedtuple("Details",["emp_id","emp_name","department","salary"])
n = int(input("Enter number of Employees: "))

Employees=[]
for i in range(n):
    print(f"Enter Employee{i+1} details: ")
    id=int(input("Enter Employee ID: "))
    name=input("Enter Employee Name: ")
    d=input("Enter Employee Department: ")
    s=float(input("Enter Employee Salary: "))
    Employees.append(Emp(id,name,d,s))

target = input("Enter Department Name: ").lower()

high_salary=Employees[0]
lowest_salary=Employees[0]
for i in range(len(Employees)):
    if Employees[i].salary>high_salary.salary:
        high_salary=Employees[i]
    elif Employees[i].salary<lowest_salary.salary:
        lowest_salary=Employees[i]
all_Sum=0
for i in range(len(Employees)):
    all_Sum+=Employees[i].salary

for i in Employees:
    print(*i)
print("\nHigh Salary Employee: \n",*high_salary)
print("\nLow Salary Employee: \n",*lowest_salary)
print("\nAverage Salary : \n", all_Sum/n)

print()
for i in range(len(Employees)):
    if Employees[i].department.lower()==target:
        print(*Employees[i])
''=====================================================================
QUESTION 3: HOSPITAL PATIENT TRACKER
====================================

A hospital stores patient records for daily monitoring.

Fields:
patient_id, patient_name, age, disease

Requirements:

1. Read N patient records from the user and store them in a list of NamedTuples.

---

2. Display all patient details.

---

3. Display patients whose age is above 60 years.

---

4. Search for a patient using Patient ID.

---

5. Count the number of patients suffering from a particular disease.

---

Test Case:

Input:
Enter number of patients: 4

P101 Rajesh 65 Diabetes
P102 Suman 45 Fever
P103 Mohan 70 Diabetes
P104 Rita 35 Cold

Enter Patient ID: P103
Enter Disease: Diabetes

Expected Output:
Patient Found:
P103 Mohan 70 Diabetes

Patients Above 60:
P101 Rajesh 65 Diabetes
P103 Mohan 70 Diabetes

Patients with Diabetes:
2
'''


from collections import namedtuple
Patient = namedtuple("Patients",["patient_id","patient_name","age","disease"])
N = int(input("Enter Number of Patients: "))

patient=[]
for i in range(N):
    print(f"Enter patient{i+1} Details: ")
    id = input("Enter Patient ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    disease = input("Enter Disease: ")
    patient.append(Patient(id,name,age,disease))


print("\n All Patient Details: ")
for i in range(N):
    print(*patient[i])
print()

p_id = input("\nEnter Patient Id: ")
p_disease = input("Enter Disease: ")


x=-1
print(f"Checking.. if Patient found with {p_id} and {p_disease}: ")
for i in range(len(patient)):
    if patient[i].patient_id==p_id and patient[i].disease==p_disease:
        print("Patient Found: ")
        print("\n",*patient[i])
    else:
        print("Patient not found ")

    
print("\n Patients Above 60: ")
for i in range(len(patient)):
    if patient[i].age>60:
        print("\n",*patient[i])

count=0
print("\n Patients with Diabetes: ")
for i in range(len(patient)):
    if patient[i].disease=="Diabetes":
       count+=1
print("",count)

'''=====================================================================
QUESTION 2: STUDENT RESULT PROCESSING
=====================================

A training institute wants to manage student records using NamedTuple.

Fields:
roll_no, name, course, marks

Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

---

2. Display all student details.

---

3. Find and display the topper of the class.

---

4. Count and display the number of students scoring above 80 marks.

---

5. Calculate and display the average marks.

---

6. Accept a course name from the user and display all students enrolled in that course.

---

Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92
'''


from collections import namedtuple
S = namedtuple("Details",["roll_no","name","course","marks"])
n = int(input("Enter number of Students: "))

Students=[]
for i in range(n):
    print(f"Enter Student{i+1} Details: ")
    r=int(input("Enter Roll No:"))
    name=input("Enter Name: ")
    c=input("Enter Course: ")
    m=int(input("Enter Marks: "))
    Students.append(S(r,name,c,m))

Course = input("Enter Course Name: ")

Topper=Students[0]
Above_80 = 0
marks_sum=0
for i in range(len(Students)):
    if Students[i].marks>Topper.marks:
        Topper=Students[i]
    if Students[i].marks>80:
        Above_80+=1
    marks_sum+=Students[i].marks


print("\nTopper: \n",*Topper)
print(f"\n Students Above 80 : \n {Above_80}")
print(f"\n Average Marks: \n {marks_sum/n}")
print(f"\nStudents in {Course} Course: ")
for i in range(len(Students)):
    if Students[i].course==Course:
        print(*Students[i])
6.

NOTE: using tuple only
An electronics store wants to maintain product information. Since product details should not be modified accidentally,
 each product record is stored as a tuple.

Tuple Format:

(product_id, product_name, price)

Requirements:

Read N product details from the user and store them as tuples in a list.
Display all product details.
Find and display the costliest product.
Find and display the cheapest product.
Calculate and display the average price of all products.
Display all products whose price is greater than ₹50,000.

Test Case:

Input:

Enter number of products: 4

P101 Laptop 65000
P102 Mobile 25000
P103 Television 80000
P104 Tablet 30000

Expected Output:

All Products:
('P101', 'Laptop', 65000)
('P102', 'Mobile', 25000)
('P103', 'Television', 80000)
('P104', 'Tablet', 30000)

Costliest Product:
('P103', 'Television', 80000)

Cheapest Product:
('P102', 'Mobile', 25000)

Average Price:
50000.0

Products Above ₹50,000:
('P101', 'Laptop', 65000)
('P103', 'Television', 80000)

7.

A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.

Tuple Format:

(player_id, player_name, runs_scored)

Requirements:

Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.

Test Case:

Input:

Enter number of players: 5

101 Virat 82
102 Rohit 45
103 Gill 120
104 Hardik 38
105 SKY 76

Expected Output:

All Players:
(101, 'Virat', 82)
(102, 'Rohit', 45)
(103, 'Gill', 120)
(104, 'Hardik', 38)
(105, 'SKY', 76)

Highest Scorer:
(103, 'Gill', 120)

Lowest Scorer:
(104, 'Hardik', 38)

Total Runs:
361

Average Runs:
72.2

Players Scoring More Than 50 Runs:
(101, 'Virat', 82)
(103, 'Gill', 120)
(105, 'SKY', 76)