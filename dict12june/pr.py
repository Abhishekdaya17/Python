# n=int(input("enter the number of patient:"))
# d={}
# for i in range(n):
#                 p_id=int(input("Enter patient id:"))
#                 nam=input("enter the name:")
#                 age=int(input("enter the age:"))
#                 disease=input("Disease:")
#                 doctor=input("doctor name:")
#                 nd={
#                     p_id:{"name":nam,"age":age,"disease":disease,"doctor":doctor}
#                 }
#                 d.update(nd)

# for k,v in d.items():
#                 print("id=",k)
#                 for l,m in v.items():
#                         print(l,":",m)
a=[1,2,3]
b=[4,5,6]
a.append(b)
print(a)
a.update(b)
print(a)