# mortgage.py
#
# Exercise 1.17
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
no_of_months = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    no_of_months = no_of_months + 1
    if ((no_of_months >= extra_payment_start_month) & (no_of_months <= extra_payment_end_month)):
        principal = principal - extra_payment
        total_paid = total_paid + payment + extra_payment
    else:
        total_paid = total_paid + payment
    # print(no_of_months, total_paid, principal)
    print(
        f'No of months: {no_of_months}, Total Paid so far: ${total_paid:0.2f}, Principal Left: ${principal:0.2f}')

print(f'Total no of months: {no_of_months}')
print(f'Total amount paid: ${total_paid:0.2f}')
