pens_count = int(input())
markers_count = int(input())
detergent_litres = int(input())
discount_percent = int(input())

pens_price = pens_count * 5.80
markers_price = markers_count * 7.20
detergent_liter_price = detergent_litres * 1.20

total_price = pens_price + markers_price + detergent_liter_price
final_price = total_price * discount_percent/100

print(total_price - final_price)
