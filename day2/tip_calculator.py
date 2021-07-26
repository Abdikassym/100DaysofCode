#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

# Let's start then...
print("Welcome to the tip calculator!")

total_bill = float(input("What is the total bill you have to pay? "))
tip = int(input("What is the tip percentage you would like to give? "))
guests = int(input("How many people are going to split the bill?"))

total_amount = total_bill + (tip / 100 * total_bill)
amount_for_each = round(total_amount / guests, 2)
amount_for_each = "{:.2f}".format(amount_for_each)

print(f"Each person should pay {amount_for_each} dollars.")



