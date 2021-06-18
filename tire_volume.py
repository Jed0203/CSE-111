import math
# Import the datatime module so that
# it can be used in this program.
from datetime import datetime

# Call the now() method to get the current date and
# time as a datetime object from the computer's clock.
current_date = datetime.today().strftime('%Y-%m-%d')

w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))

v = (math.pi * (w ** 2) * a * ((w * a) + (2540 * d))) / 10000000
print(f"The approximate volume is {v:.1f} cubic cm.")
if w == 185 and a == 55 and d == 15:
  print("The price of this tire size would be: $85.49")
elif w == 185 and a == 70 and d == 14:
  print("The price of this tire size would be: $45.99")
elif w == 275 and a == 40 and d == 20:
  print("The price of this tire size would be: $167.39")
  #price = 167.39
elif w == 225 and a == 70 and d == 14:
  print("The price of this tire size would be: $97.99")
  #price = 97.99

buy_tire = True
while buy_tire == True:
  continue_on = input("Would you like to buy this tire ? Type no if finished.: ")

  if continue_on.lower() == "no":
    buy_tire = False
  elif continue_on.lower() == "yes":
    phone_number = input("What is your phone number?")
    

# Open a text file named dimensions.txt in append mode.
with open("dimensions.txt", "at") as dimens_file:

    # Print a car's model and dimensions to the file.
    print(f"{current_date},{w}, {a}, {d}, {v:.1f}, {phone_number}", file=dimens_file)