# Taking in Marks on 3 Subjects
m1 = float(input("Enter marks of first subject: "))
m2 = float(input("Enter marks of second subject: "))
m3 = float(input("Enter marks of third subject: "))

# Taking in Credits on 3 Subjects
c1 = int(input("Enter credits of first subject: "))
c2 = int(input("Enter credits of second subject: "))
c3 = int(input("Enter credits of third subject: "))

# Grade Point Calculation
mg1 = m1//10
mg2 = m2//10
mg3 = m3//10

# CGPA Calculation and Display
gpa=((mg1*c1+mg2*c2+mg3*c3)/(c1+c2+c3))+1
print(gpa)