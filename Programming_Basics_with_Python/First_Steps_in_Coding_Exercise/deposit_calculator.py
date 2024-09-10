deposit_amount = float(input())
term_of_deposit = int(input())
annual_rate = float(input())

annual_interest_amount = deposit_amount * annual_rate / 100
monthly_interest_amount = annual_interest_amount / 12
total_amount = deposit_amount + term_of_deposit * monthly_interest_amount

print(total_amount)

