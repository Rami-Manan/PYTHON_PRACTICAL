print('Welcome to the tution fees calculator!')  # Welcome message

Tution_Fees = float(input('Enter your tution fees ='))  # Enter your tuition fees
Deposit = float(input('Enter deposit percentage ='))  # Enter the deposit percentage
Discount = float(input('Enter discount percentage ='))  # Enter the discount percentage


Discount_Value = (Tution_Fees * Discount) / 100  # Calculate discount value from percentage
Discounted_Tution_Fees = Tution_Fees - Discount_Value  # Tuition fees after discount
print('The value of discount =', Discount_Value)
print('The tuition fees after discount =', Discounted_Tution_Fees)

Total_Deposit = (Discounted_Tution_Fees * Deposit) / 100  # Calculate deposit from discounted tuition fees
print('The value of deposit =', Total_Deposit)  # Show the deposit amount

Installment_1 = float(input('Enter installment amount ='))  # Enter the installment amount
Total_Remaining_Amount_1 = Discounted_Tution_Fees - Total_Deposit - Installment_1  # Remaining amount after discount, deposit, and installment
print('The remaining amount =', Total_Remaining_Amount_1)

Installment_2 = float(input('Enter installment amount ='))  # Enter the installment amount
Total_Remaining_Amount_2 = Total_Remaining_Amount_1 - Installment_2  # Remaining amount after deposit and installments
print('The remaining amount =', Total_Remaining_Amount_2)

Installment_3 = float(input('Enter installment amount ='))  # Enter the installment amount
Total_Remaining_Amount_3 = Total_Remaining_Amount_2 - Installment_3  # Remaining amount after deposit and installments
print('The remaining amount =', Total_Remaining_Amount_3)
