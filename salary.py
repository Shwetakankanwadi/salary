import sys

if(len(sys.argv))==2:
  script_name = sys.argv[0]   
  salary = float(sys.argv[1])  
else:
  salary =900

bonus = salary * 0.10
total_salary = salary + bonus
print("Employee Salary:", salary)
print("Bonus (10%):", bonus)
print("Total Salary After Bonus:",total_salary)
