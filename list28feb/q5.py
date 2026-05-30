'''

5.
 Student Grade Classification System (Python List Assignment)


A school stores student marks in a list. The system must analyze the marks and generate a **clear performance report** 
by grouping students into grade categories.



Write a Python program to:

* Iterate through the list of marks
* Assign grades based on marks:

  * **>= 90 → A**
  * **>= 75 and < 90 → B**
  * **>= 50 and < 75 → C**
  * **< 50 → Fail**
* Store each category in separate lists
* Count students in each category
* Display a **final structured report (important)**

---

## 📌 Output Format (Mandatory)

Your output must be displayed exactly in this format:

```
===== STUDENT GRADE REPORT =====

A Grade Students   : [list]
B Grade Students   : [list]
C Grade Students   : [list]
Fail Students      : [list]

--------------------------------
A Count   : X
B Count   : X
C Count   : X
Fail Count: X
--------------------------------

Total Students: X
```

---

 Input

[95, 82, 67, 45, 30]

Output

```
===== STUDENT GRADE REPORT =====

A Grade Students   : [95]
B Grade Students   : [82]
C Grade Students   : [67]
Fail Students      : [45, 30]

--------------------------------
A Count   : 1
B Count   : 1
C Count   : 1
Fail Count: 2
--------------------------------

Total Students: 5
'''
n=int(input("number of students:"))
marks=[]
for i in range(n):
    # str=map(str,input("enter the marks:").split())
    str=int(input("enter the marks="))
    marks.append(str)
a=[]
ca=0
b=[]
cb=0
c=[]
cc=0
fail=[]
fc=0
for i in marks:
    if i>=90:
        a.append(i)
        ca=ca+1
        
    elif i>=75 and i<90:
        b.append(i)
        cb=cb+1
    elif i>=50 and i<75:
    
        c.append(i)
        cc=cc+1
    else:
        fail.append(i)
        fc=fc+1
print("========student report card=======")
print("A Grade Students   :",a)
print("B Grade Students   :",b)
print("C Grade Students   :" ,c)
print("Fail Students      :",fail)
print("--------------------")
print("A Count   :",ca)
print("B Count   :",cb)
print("C Count   :", cc)
print("Fail Count:",fc)
print("---------------------")
print("total students=",n)