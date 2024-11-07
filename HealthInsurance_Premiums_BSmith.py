"""Author Brian Smith"""
# Program: Health Insurance Premiums

def calculate_premium(emp_id, has_primary_care, had_physical, is_non_smoker, has_gym_membership, selects_biweekly):
    # base premium
    base_premium = 800 if has_primary_care == 'Y' else 1000
    
    # discount variables
    physical_discount = 20 if had_physical == 'Y' else 0
    smoker_discount = 60 if is_non_smoker == 'Y' else 0
    gym_discount = 10 if has_gym_membership == 'Y' else 0
    
    # total monthly premium after discounts
    total_discount = physical_discount + smoker_discount + gym_discount
    total_premium = base_premium - total_discount
    
   # Calculate bi-weekly payment if selected
    if selects_biweekly == 'Y':
        biweekly_payment = total_premium * 0.99 / 2  # Apply 1% discount for bi-weekly payment
    else:
        biweekly_payment = None
    
    # display output
    print(f"EmpID: {emp_id}")
    print(f"Base monthly premium: ${base_premium}")
    print("Discounts:")
    if physical_discount:
        print(f"  Physical/labs: ${physical_discount}")
    if smoker_discount:
        print(f"  Non-smoker: ${smoker_discount}")
    if gym_discount:
        print(f"  Gym: ${gym_discount}")
    print(f"Total Premium: ${total_premium:.2f}")
    if biweekly_payment:
        print(f"Bi-weekly payment: ${biweekly_payment:.2f}")

# input collection 
employee_id = input("Enter employee ID: ")
has_primary_care = input("Primary care physician (Y/N): ")
had_physical = input("Annual physical exam & labs (Y/N): ")
is_non_smoker = input("Non-smoker (Y/N): ")
has_gym_membership = input("YMCA gym membership (Y/N): ")
selects_biweekly = input("Bi-weekly payment (Y/N): ")

# Call the function w the inputs
calculate_premium(employee_id, has_primary_care, had_physical, is_non_smoker, has_gym_membership, selects_biweekly)
