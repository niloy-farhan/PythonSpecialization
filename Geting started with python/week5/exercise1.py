hrs = input("Enter Hours:")
pph = input("Enter rate per hour:")
h = float(hrs)
pr = float(10.50)

over_hp = 1.5

if h <= 40:
    payment = h * pr
    print(payment)
elif h > 40:
    regular_hours = 40
    overtime_hours = h - regular_hours
    regular_payment = regular_hours * pr
    overtime_payment = overtime_hours * pr * over_hp
    total_payment = regular_payment + overtime_payment
    print(total_payment)
else:
    print("Invalid entry")
