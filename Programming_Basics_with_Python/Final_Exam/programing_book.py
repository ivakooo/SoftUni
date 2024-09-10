price_per_page = float(input())
price_per_cover = float(input())
percent_discount_for_paper_print = int(input())
designer_price = float(input())
percent_from_total_paid_sum = int(input())

PAGES = 899
COVERS = 2

initial_sum = price_per_page * PAGES + price_per_cover * COVERS
price_with_discount = initial_sum * (100 - percent_discount_for_paper_print) / 100
price_with_designer_tax = price_with_discount + designer_price
total_money = price_with_designer_tax * (100 - percent_from_total_paid_sum) / 100

print(f"Avtonom should pay {total_money:.2f} BGN.")
