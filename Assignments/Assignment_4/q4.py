Item = "Gloves"
Price = 35.50
Quantity = 9

subtotal = Price * Quantity
tax_amount = subtotal * 0.05
total = subtotal + tax_amount

print(f"Subtotal: {subtotal:.2f}")
print(f"Tax: {tax_amount:.2f}")
print(f"Total: {total:.2f}")