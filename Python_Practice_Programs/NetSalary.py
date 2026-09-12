BS = int(input("Enter ypur Basic Salary: "))

HRA = 20*BS/100
print("House Rent Allowance is: ", HRA)
DA = 40*BS/100
print("Dearness Allowance is: ", DA)

GS = BS + HRA + DA
print("Gross Salary is: ", GS)

PF = 10*GS/100
print("Provident Fund is: ", PF)

NS = GS - PF
print("Net Salary is: ", NS)