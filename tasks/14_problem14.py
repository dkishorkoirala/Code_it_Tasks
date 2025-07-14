unit = int(input("Enter the electricity unit: "))

fixed_charge = 30
t_price = 0

if unit <= 20:
    t_price = fixed_charge

elif unit <= 50:
    t_price = fixed_charge + (unit - 20) * 4

elif unit <= 150:
    t_price = fixed_charge + (30 * 4) + (unit - 50) * 7.30

elif unit <= 250:
    t_price = fixed_charge + (30 * 4) + (100 * 7.30) + (unit - 150) * 8.60

elif   unit > 250:
    t_price = fixed_charge + (30 * 4) + (100 * 7.30) + (100 * 8.60) + (unit - 250) * 9.50

else:
    print("Invalid input")
    
print("Total Electricity Bill: Rs.", round(t_price, 2))
