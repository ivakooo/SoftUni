needed_safety_nylon = int(input())
needed_paint_in_liters = int(input())
needed_paint_thinner_in_liters = int(input())
needed_working_hours = int(input())

safety_nylon_price = ((needed_safety_nylon + 2) * 1.5)
paint_price = ((needed_paint_in_liters + needed_paint_in_liters * 0.1) * 14.50)
paint_thinner_price = (needed_paint_thinner_in_liters * 5.00)
bags_price = float(0.40)
total_materials_price = safety_nylon_price + paint_price + paint_thinner_price + bags_price
workers_price_per_hour = total_materials_price * 0.3
workers_total_price = workers_price_per_hour * needed_working_hours

print(total_materials_price + workers_total_price)
