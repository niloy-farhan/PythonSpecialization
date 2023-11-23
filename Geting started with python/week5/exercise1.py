hrs = input("Enter Hours:")
pph = input("Enter rate per hour:")
h = float(hrs)
pr = float(10.50)

over_hp = 1.5

if (h <= 40):
    payment = h * pr
    print(payment)

elif (h > 40):
    payment = 40.0 * pr
    opayment = (40 - h) * over_hp
    print(opayment)
    t_Payment = payment + opayment
    print(t_Payment)

else:
    print("Invalid entry")