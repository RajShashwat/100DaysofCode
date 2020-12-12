age = int(input("Enter your age: "))

years_left = 100 - age

days_left = years_left * 365
month_left = years_left * 12
weeks_left = years_left * 52

message = f"You have:\n{years_left} years,\n{month_left} months,\n{weeks_left} week,\n{days_left} days,\nleft to complete 100 years"

print(message)