print("Student Marks And Grades:")
s=[88,75,92,45,65,82,91,64,87,71]
g=[]
for i in s:
    if (i>90 and i<100):
        g.append("A")
    elif (i>80 and i<90):
        g.append("B")
    elif (i>70 and i<80):
        g.append("C")
    elif (i>60 and i<70):
        g.append("D")
    elif (i>50 and i<60):
        g.append("E")
    elif (i<50):
        g.append("F")
j=0
while j<len(s):
    print(f"student{j+1}:marks={s[j]}  Grade={g[j]}")
    j+=1



    