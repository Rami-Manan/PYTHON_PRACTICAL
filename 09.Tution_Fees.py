print('Welcome to the tution fees calculator!')  # Welcome message

Tution_Fees = float(input('Enter your tution fees ='))  # Enter your tuition fees
Deposit = float(input('Enter deposit percentage ='))  # Enter the deposit percentage

Total_Deposit = (Tution_Fees  * Deposit ) / 100  # Calculate deposit value from percentage
print('The value of deposit =', Total_Deposit)  # Show the deposit amount

Installment_1 = float(input('Enter installment amount ='))  # Enter the installment amount
Total_Remaining_Amount_1 = Tution_Fees - Total_Deposit - Installment_1  # Remaining amount after deposit and installment
print('The remaining amount =', Total_Remaining_Amount_1)

Installment_2 = float(input('Enter installment amount ='))  # Enter the installment amount
Total_Remaining_Amount_2 = Total_Remaining_Amount_1 - Installment_2  # Remaining amount after deposit and installments
print('The remaining amount =', Total_Remaining_Amount_2)

Installment_3 = float(input('Enter installment amount ='))  # Enter the installment amount
Total_Remaining_Amount_3 = Total_Remaining_Amount_2 - Installment_3  # Remaining amount after deposit and installments
print('The remaining amount =', Total_Remaining_Amount_3)
