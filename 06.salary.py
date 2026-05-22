salary = float(input('Enter your salary =  '))       # Enter your salary  
TDS = float(input('Enter TDS percentage =  '))    # enter your TDS

TAX = float(input('Enter TAX percentage =  '))    # enter your tax 

TDS_ = (salary * TDS) / 100  # here we are multiplication the  TDS and the salary  then for percentage we will divide it from 100 
print('The value of TDS_ =',TDS_) # This will show the value of TDS_

TAX_ = (salary * TAX ) / 100  # here we are multiplication the  TAX and the salary  then for percentage we will divide it from 100
print('The value of TAX_ =',TAX_) # This will show the value of TAX_

In_hand_salary = salary -TDS_ - TAX_ # here we will  do subtraction of the value of salary , tds , tax

print('In Hand Salary ', In_hand_salary) # this is a in hand salary after subracting TDS and tax 

