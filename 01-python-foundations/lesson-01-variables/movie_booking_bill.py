# 1. Basic details
theater = "Star Cinema"
customer = "Neha"
movie = "Space Journey"
ticket_price = 250
ticket_qty = 4
popcorn_price = 180.5
popcorn_qty = 2
convenience_fee = 35
coupon_discount = 50
payment_mode = "Card"
is_booked = True
people = 4

# 2. Python calculation
ticket_total = ticket_price * ticket_qty
popcorn_total = popcorn_price * popcorn_qty
total = ticket_total + popcorn_total + convenience_fee - coupon_discount
per_person = total / people

# 3. Print
print(theater)
print(f"Customer: {customer}")
print(f"Movie: {movie}")
print(f"Tickets x {ticket_qty} = ₹{ticket_total}")
print(f"Popcorn x {popcorn_qty} = ₹{popcorn_total}")
print(f"Convenience fee = ₹{convenience_fee}")
print(f"Discount = -₹{coupon_discount}")
print(f"Total = ₹{total}")
print(f"Per person ({people}) = ₹{per_person}")
print(f"Payment: {payment_mode} | Booked: {is_booked}")

# 4. Types
print(type(theater))
print(type(ticket_total))
print(type(popcorn_total))
print(type(per_person))
print(type(is_booked))
