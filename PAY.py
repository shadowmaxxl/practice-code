hours=int(input("enter the number of hours you worked"))
rate=int(input("enter your hourly rate"))
try:
  if hours<=40:
    pay=hours*rate
  else:
    pay=(((hours-40)*1.5)*rate)+(40*rate)
  print("your pay is",pay)
except ValueError:
  print("please enter a valid number")