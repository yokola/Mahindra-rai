#condtion type
print("F=ma *2nt law")
#determining the missing value 
print("select the missing vale: ")
print("1.mass(m)")
print("2.acceleration(a)")
print("3.Force(F)")
missing_value_choice= input ("enter the option number for the missing value:")

#user input 
if missing_value_choice =="1":
    a = float (input("enter acceleration(a): "))
    F = float(input("enter force(F): "))
    m = F/a
    print(f"mass (m)= {m}")
elif missing_value_choice =="2":
    m = float(input("enter mass (M): "))
    F = float(input("enter force(f): "))  
    a =F/m
    print(f"acceleration(a): {a}")  
elif missing_value_choice == "3":
    m = float (input("enter mass (m): "))
    a = float(input("acceleration(a): "))
    F = m*a 
    print(f"force (F): (F)")
    print(f"acceleration(a): {F}")
else :
    print("entered number is invaild.")    

