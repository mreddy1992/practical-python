# bounce.py
#
# Exercise 1.5
height = 100  # Metres
num_of_bounces = 0

while num_of_bounces < 10:
    height = (3 / 5) * height
    num_of_bounces += 1
    print(num_of_bounces, round(height, 4))




