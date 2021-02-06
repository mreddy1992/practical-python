# mortgage.py
#
# Exercise 1.8
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
no_of_months = 0

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    no_of_months = no_of_months + 1
    if (no_of_months <= 12):
        principal = principal - 1000
        total_paid = total_paid + payment + 1000
    else:
        total_paid = total_paid + payment

print('No of months', no_of_months)
print('Total paid', total_paid)
