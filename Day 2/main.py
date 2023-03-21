#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip caluclator.")
total_bill = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? ")
how_many_people = input("How many people to split the bill? ")
person_pay = round( (float(total_bill) / int(how_many_people)) * (float(tip) / 100 + 1) ,2 )
print(f"Each person should pay: ${person_pay}")

#(bill / how_many_people) * tip (ex: 1.12)