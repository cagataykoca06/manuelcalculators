hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices:
  total_price += price

print(total_price)

average_price = (total_price / len(prices))
print("Average Haircut Price: " + str(average_price))


new_prices = [] 
for new_price in prices:
  x = new_price - 5
  new_prices.append(x)

print(new_prices)


total_revenue = 0
diversity = len(hairstyles)
diversity_list = list(range(diversity))



for i in range (0, diversity):
  total_revenue += prices[i] * last_week[i]

print("Total Revenue: " + str(total_revenue))
  
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)


cuts_under_30 = []
for i in range (0, diversity):
  if new_prices[i] < 30:
    cuts_under_30.append(hairstyles[i])

print(cuts_under_30)







