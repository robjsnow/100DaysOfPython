#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip caluclator.")
total_bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? "))
how_many_people = int(input("How many people to split the bill? "))

person_pay = (total_bill / how_many_people) * (tip / 100 + 1)
print(f"Each person should pay: ${person_pay: .2f}")

#(bill / how_many_people) * tip (ex: 1.12)