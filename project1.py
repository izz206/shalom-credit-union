import pandas as pd

#eligibility criteria
age = 55
duration = 10
monthly_income = 10000

if age >= 55 and duration >= 5 and monthly_income >= 10000:
    is_eligible = True
elif age < 55 or duration < 5 or monthly_income < 10000:
    is_eligible = True
else:
    is_eligible = False



#loan approval
good_credit_score = True
good_employment_status = True
good_income_history = True

if good_credit_score and good_employment_status and good_income_history:
    loan_approval = True
else:
    loan_approval = False

if is_eligible and loan_approval == True:
    print("Congratulations! You have been approved for a loan")

else:
    print("Sorry, you are not eligible for a loan")