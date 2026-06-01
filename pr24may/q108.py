'''108 Check if a string is an isogram (no repeating letters). S = "ambidextrous" TRUE
'''
# s=input("input:").lower()
# alp=""
# flag=False
# for i in range(len(s)):
#     ch=s[i]
#     if ch>="a" and ch<="z":
#         if ch not in alp:
#             alp=alp+ch
#             flag=True
# if flag:
#     print("true")
# else:
#     print("false")
s = input("input: ").lower()

seen = ""
is_iso = True

for i in range(len(s)):
    ch = s[i]

    if ch >= "a" and ch <= "z":

        if ch in seen:
            is_iso = False
            break
        else:
            seen = seen + ch

if is_iso:
    print("true")
else:
    print("false")

