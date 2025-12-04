
bill = float(input("What is the total bill? $ "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))


totall = round((bill + (bill * (tip_percentage / 100))) / num_people, 2)
print(f"Each person should pay: ${totall}")